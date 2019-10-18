from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.contrib import messages
from .forms import ProjectProposalForm, EditProject, UnitProjectLinkForm, UnitForm
from .models import ProjectModel, UnitProjectLink, UnitModel
from user.models import Profile, User
from django.db.models import F
import csv


# Home Page
@login_required(login_url='/login/')
def home(request):
    # If the user is a superuser/admin, their home page will be the admin dashboard
    # If they're a normal user, they will redirected to their own dashboard
    if request.user.is_superuser:
        # The following conditional statements are for filtering the projects
        if request.GET.get('degree'):
            project_filter = request.GET.get('degree')
            projectList1 = ProjectModel.objects.filter(postgraduate=project_filter, draft=False).order_by(F('submissionDate').asc())
            projects = projectList1
        else:
            projectList1 = ProjectModel.objects.filter(draft=False).order_by(F('submissionDate').asc())
            projects = projectList1
        if request.GET.get('unit'):
            unitID = request.GET.get('unit')
            unitCodes = UnitModel.objects.filter(unitCode=unitID)
            IDset = []
            for i in unitCodes:
                IDset.append(i.unitID)
            LinkSet = UnitProjectLink.objects.filter(unitID__in=IDset)
            projectList2 = []
            for i in LinkSet:
                projectList2.append(i.projectID)
            projects = list(set(projectList1).intersection(projectList2))

        usersToBeAuthenticated = User.objects.filter(is_active=False).order_by(F('date_joined').desc())

        unitLinks = UnitProjectLink.objects.all()

        if request.method == 'POST':
            # The following forms conditional statements are for when creating unit links, deleting links and adding units respectively
            form = UnitProjectLinkForm(request.POST)
            if 'Add' in request.POST:
                if form.is_valid():
                    formData = UnitProjectLink()
                    formData.projectID = form.cleaned_data['projectID']
                    formData.unitID = form.cleaned_data['unitID']
                    try:
                        formData.save()
                        messages.success(request, f'Link between {formData.projectID} and {formData.unitID} created')
                        return redirect('home-page')
                    except:
                        messages.error(request,
                                       f'Link between {formData.projectID} and {formData.unitID} already exists')
                        return redirect('home-page')
            elif 'Delete' in request.POST:
                if form.is_valid():
                    project = form.cleaned_data['projectID']
                    unit = form.cleaned_data['unitID']
                    try:
                        UnitProjectLink.objects.filter(projectID=project, unitID=unit).get()
                        UnitProjectLink.objects.filter(projectID=project, unitID=unit).delete()
                        messages.success(request, f'Link between {project} and {unit} removed')
                    except:
                        messages.error(request, f'Link between {project} and {unit} does not exist')
                    return redirect('home-page')
            elif 'Extra' in request.POST:
                unit_registration(request)

        form = UnitProjectLinkForm()
        form2 = UnitForm()
        units = UnitModel.objects.all()

        # Creating a page table for the project proposals
        page = request.GET.get('page', 1)

        paginator = Paginator(projects, 5)
        try:
            projectsList = paginator.page(page)
        except PageNotAnInteger:
            projectsList = paginator.page(1)
        except EmptyPage:
            projectsList = paginator.page(paginator.num_pages)

        context = {
            'all_projects': projectsList,
            'usersToBeAuthenticated': usersToBeAuthenticated,
            'form': form,
            'form2': form2,
            'unitLinks': unitLinks,
            'units': units
        }
        return render(request, 'admin-home.html', context=context)

    projectList = ProjectModel.objects.filter(supervisor1=request.user)
    return render(request, 'home.html', {'projectList': projectList})


# Project list page
# Including the filter for different education level and units
def project_list(request):
    if request.GET.get('degree'):
        project_filter = request.GET.get('degree')
        projectList1 = ProjectModel.objects.filter(postgraduate=project_filter, draft=False, archived=False,
                                                   approved=True).order_by(F('submissionDate').asc())
        projects = projectList1
    else:
        projectList1 = ProjectModel.objects.filter(draft=False, archived=False, approved=True).order_by(F('submissionDate').asc())
        projects = projectList1
    if request.GET.get('unit'):
        unitID = request.GET.get('unit')
        unitCodes = UnitModel.objects.filter(unitCode=unitID)
        IDset = []
        for i in unitCodes:
            IDset.append(i.unitID)
        LinkSet = UnitProjectLink.objects.filter(unitID__in=IDset)
        projectList2 = []
        for i in LinkSet:
            projectList2.append(i.projectID)
        projects = list(set(projectList1).intersection(projectList2))

        # If the export button is pressed, write all filtered projects into a CSV, then download it for the user
    if request.GET.get('Export'):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Exported_Projects.csv"'

        writer = csv.writer(response)

        writer.writerow(["Project ID", "Approved", "Archived", "Draft", "Postgraduate", "Submission Date", "Supvervisor 1", "Supervisor 2 Title", "Supervisor 2 First Name", "Supervisor 2 Last Name", "Supervisor 3 Title", "Supervisor 3 First Name", "Supervisor 3 Last Name", "Title", "Description", "Number of Students", "Prerequisites", "Project Tags", "IP", "On Campus", "Chemical", "Civil", "Electrical", "Environmental", "Materials", "Mechanical", "Mechatronic", "Mining", "Oil and Gas", "Petroleum", "Software", "Other"])

        for p in projects:
            writer.writerow([p.projectID, p.approved, p.archived, p.draft, p.postgraduate, p.submissionDate, p.supervisor1, p.supervisor2Title, p.supervisor2FirstName, p.supervisor2LastName, p.supervisor3Title, p.supervisor3FirstName, p.supervisor3LastName, p.title, p.description, p.noOfStudents, p.prerequisites, p.projectTags, p.IP, p.onCampus, p.chemical, p.civil, p.elec, p.envir, p.materials, p.mechanical, p.mechatronic, p.mining, p.oilGas, p.petroleum, p.software, p.other])

        return response

    page = request.GET.get('page', 1)

    # If description of the project is longer than 100 characters, then remove trailing empty space and add "..."
    for i in range(len(projects)):
        if len(projects[i].description) > 100:
            projects[i].description = str(projects[i].description[:100]).strip() + "..."

    paginator = Paginator(projects, 5)
    try:
        projectsList = paginator.page(page)
    except PageNotAnInteger:
        projectsList = paginator.page(1)
    except EmptyPage:
        projectsList = paginator.page(paginator.num_pages)

    units = UnitModel.objects.all()

    tagsList = []

    # The following for loops split up the tags from the spring into separate words
    # They are stored as a list back into the projectTags field of the each project

    for i in range(len(projectsList)):
        tagsList.append(projectsList[i].projectTags)

    for j in range(len(tagsList)):
        tags = tagsList[j].split(", ")
        i = 0
        while i < len(tags):
            tags[i] = tags[i].strip(', ')
            if tags[i] == "":
                tags.pop(i)
            else:
                i += 1
        tagsList[j] = tags

    for i in range(len(projectsList)):
        projectsList[i].projectTags = tagsList[i]

    context = {
        'all_projects': projectsList,
        'units': units,
    }
    return render(request, 'project_list.html', context=context)


# Project details page
def project_detail(request, pk):
    project = ProjectModel.objects.get(pk=pk)
    username = request.user.username
    creator = project.supervisor1.id
    supervisor = Profile.objects.get(user_id=creator)

    strUser = str(username)
    strSupervisor = str(supervisor.user)

    # Check if the project is still a draft, and if so only let the supervisor view it
    if project.draft is True and strUser != strSupervisor:
        return render(request, 'denied.html')
    elif project.archived is True and not request.user.is_superuser and strUser != strSupervisor:
        return render(request, 'denied.html')
    else:
        # Break up the prerequisites at the commas and tags up at the commas and spaces
        prereqs = project.prerequisites.split(",")
        i = 0
        while i < len(prereqs):
            prereqs[i] = prereqs[i].strip()
            if prereqs[i] == "":
                prereqs.pop(i)
            else:
                i += 1

        tags = project.projectTags.split(", ")
        i = 0
        while i < len(tags):
            tags[i] = tags[i].strip(', ')
            if tags[i] == "":
                tags.pop(i)
            else:
                i += 1

        unitlinks = UnitProjectLink.objects.values_list('unitID', flat=True).filter(projectID=pk)
        units = []
        for link in unitlinks:
            units.append(UnitModel.objects.values_list('unitCode').get(unitID=link)[0])
        context = {
            'project': project,
            'supervisor': supervisor,
            'prereqs': prereqs,
            'tags': tags,
            'units': units
        }
    return render(request, 'project_detail.html', context=context)


# Project registration page
@login_required(login_url='/login/')
def project_registration(request):
    # This function renders the project registration page and handles the POST request
    # When a POST request is made, depending on which button is pressed, it is either
    # Saved as a draft or is submitted
    if request.method == 'POST':
        form = ProjectProposalForm(request.POST)
        if form.is_valid():
            formData = ProjectModel()
            formData.supervisor1 = request.user
            formData.supervisor2Title = form.cleaned_data['supervisor2Title']
            formData.supervisor2FirstName = form.cleaned_data['supervisor2FirstName']
            formData.supervisor2LastName = form.cleaned_data['supervisor2LastName']
            formData.supervisor3Title = form.cleaned_data['supervisor3Title']
            formData.supervisor3FirstName = form.cleaned_data['supervisor3FirstName']
            formData.supervisor3LastName = form.cleaned_data['supervisor3LastName']
            formData.title = form.cleaned_data['title']
            formData.description = form.cleaned_data['description']
            formData.noOfStudents = form.cleaned_data['noOfStudents']
            formData.prerequisites = form.cleaned_data['prerequisites']
            formData.projectTags = form.cleaned_data['projectTags']
            formData.onCampus = form.cleaned_data['onCampus']
            formData.IP = form.cleaned_data['IP']
            # Checkboxes
            formData.chemical = form.cleaned_data['chemical']
            formData.civil = form.cleaned_data['civil']
            formData.elec = form.cleaned_data['elec']
            formData.envir = form.cleaned_data['envir']
            formData.materials = form.cleaned_data['materials']
            formData.mechanical = form.cleaned_data['mechanical']
            formData.mechatronic = form.cleaned_data['mechatronic']
            formData.mining = form.cleaned_data['mining']
            formData.oilGas = form.cleaned_data['oilGas']
            formData.petroleum = form.cleaned_data['petroleum']
            formData.software = form.cleaned_data['software']
            formData.other = form.cleaned_data['other']

            # If the project is saved as a draft, update the project information to match
            title = form.cleaned_data.get('title')
            if 'Draft' in request.POST:
                formData.draft = 'True'
                messages.success(request, f'Project Proposal Draft {title} was created!')
            else:
                formData.draft = 'False'
                messages.success(request, f'Project Proposal named {title} was submitted!')

            formData.submissionDate = timezone.now()
            formData.save()
            return redirect('home-page')
    else:
        form = ProjectProposalForm()

    return render(request, 'project_registration.html', {'form': form})


# Function for editing a project
@login_required(login_url='/login/')
def project_edit(request, pk):
    # Find the requested project
    project = get_object_or_404(ProjectModel, projectID=pk)

    user = request.user.username
    creator = project.supervisor1.id
    supervisor = Profile.objects.get(user_id=creator)

    strUser = str(user)
    strSupervisor = str(supervisor.user)

    # Check if the user trying to edit the project has permission,
    # or if the project is allowed to be edited (a draft)
    if strSupervisor != strUser:
        if not project.draft:
            if not request.user.is_superuser:
                return render(request, 'denied.html')
        else:
            return render(request, 'denied.html')

    form = EditProject(request.POST or None, request.FILES or None, instance=project)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')

            if 'Draft' in request.POST:
                project.draft = True
                project.save()
                messages.success(request, f'Project Proposal Draft {title} was updated!')
                return redirect('home-page')
            else:
                project.draft = False
                project.submissionDate = timezone.now()
                project.save()

                # Return appropriate message to user
                if request.user.is_superuser:
                    messages.success(request, f'Project Proposal Draft {title} was edited!')
                else:
                    messages.success(request, f'Project Proposal Draft {title} was submitted!')
                return redirect('home-page')

    else:
        form = EditProject(instance=project)
    return render(request, 'project-edit.html', context={'form': form})


# Process for registering a unit
@login_required(login_url='/login/')
def unit_registration(request):
    # This
    if request.user.is_superuser:
        if request.method == 'POST':
            form = UnitForm(request.POST)
            if form.is_valid():
                formdata = UnitModel()
                formdata.unitCode = form.cleaned_data['unitCode']
                unitCode = form.cleaned_data['unitCode']
                try:
                    formdata.save()
                    messages.success(request, f'The unit {unitCode} has been added to the system!')
                except:
                    messages.error(request, f'The unit {unitCode} already exists!')
                return redirect('home-page')
    else:
        return render(request, 'denied.html')
    return redirect('home-page')


# Process for deleting a project
@login_required(login_url='/login/')
def project_delete(request, pk):
    projectDelete = get_object_or_404(ProjectModel, projectID=pk)

    user = request.user.username
    creator = projectDelete.supervisor1.id
    supervisor = Profile.objects.get(user_id=creator)

    strUser = str(user)
    strSupervisor = str(supervisor.user)

    # Check if the user trying to delete the project has the appropriate permission
    if strSupervisor != strUser or projectDelete.draft == False:
        if not request.user.is_superuser:
            return render(request, 'denied.html')
        elif request.user.is_superuser:
            links = UnitProjectLink.objects.filter(projectID=pk)
            if links:
                words = ""
                project = str(ProjectModel.objects.values_list('title').get(projectID=pk)[0])
                if len(links) == 1:
                    words = str(UnitModel.objects.values_list('unitCode').get(unitID=links[0].unitID.unitID)[0])
                elif len(links) == 2:
                    words = str(UnitModel.objects.values_list('unitCode').get(unitID=links[0].unitID.unitID)[0])
                    words += " and " + str(
                        UnitModel.objects.values_list('unitCode').get(unitID=links[1].unitID.unitID)[0])
                else:
                    for i in range(len(links) - 2):
                        words += str(
                            UnitModel.objects.values_list('unitCode').get(unitID=links[i].unitID.unitID)[0]) + ", "
                    words += str(
                        UnitModel.objects.values_list('unitCode').get(unitID=links[len(links) - 2].unitID.unitID)[0])
                    words += " and " + str(
                        UnitModel.objects.values_list('unitCode').get(unitID=links[len(links) - 1].unitID.unitID)[0])
                words += ". Please remove all links before removing projects."
                messages.error(request, f'The project: {project} is still linked with {words}')
            else:
                projectDelete.delete()
                messages.success(request, "Project sucessfully deleted")
    else:
        projectDelete.delete()

    return redirect('home-page')


# Approve or unapprove a project function
@login_required(login_url='/login/')
def project_approval(request, pk):
    project = get_object_or_404(ProjectModel, projectID=pk)

    # Check if the user is a superuser or not
    if not request.user.is_superuser or project.draft != False:
        return render(request, 'denied.html')

    if not project.approved:
        project.approved = True
    else:
        project.approved = False

    project.save()

    return redirect('home-page')


# List or archive a certain project
@login_required(login_url='/login/')
def project_viewable(request, pk):
    project = get_object_or_404(ProjectModel, projectID=pk)

    # Check if the user is a superuser or not
    if not request.user.is_superuser or project.draft != False:
        return render(request, 'denied.html')

    if not project.archived:
        project.archived = True
    else:
        project.archived = False

    project.save()

    return redirect('home-page')


# Set the project to be an undergraduate project or postgraduate
@login_required(login_url='/login/')
def project_postgrad(request, pk):
    project = get_object_or_404(ProjectModel, projectID=pk)

    # Check if the user is a superuser or not
    if not request.user.is_superuser or project.draft != False:
        return render(request, 'denied.html')

    if not project.postgraduate:
        project.postgraduate = True
    else:
        project.postgraduate = False

    project.save()

    return redirect('home-page')


def page_not_found(request, exception):
    context = {}
    return render(request, '404_notfound.html', context, status=404)