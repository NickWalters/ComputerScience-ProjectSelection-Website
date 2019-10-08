from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect ,get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .forms import ProjectProposalForm, EditProject, UnitProjectLinkForm, UnitForm
from .models import ProjectModel, UnitProjectLink, UnitModel
from user.models import Profile, User
import datetime

# Home Page
@login_required(login_url='/login/')
def home(request):
    if request.user.is_superuser:
        if request.GET.get('degree'):
            project_filter = request.GET.get('degree')
            projectList1 = ProjectModel.objects.filter(postgraduate=project_filter, draft=False)
            projects = projectList1
        else:
            projectList1 = ProjectModel.objects.filter(draft=False)
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
        usersToBeAuthenticated = User.objects.filter(is_active=False)[:3]
        if request.method == 'POST':
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
                        messages.error(request, f'Link between {formData.projectID} and {formData.unitID} already exists')
                        return redirect('home-page')
            elif 'Delete' in request.POST:
                if form.is_valid():
                    project = form.cleaned_data['projectID']
                    unit = form.cleaned_data['unitID']
                    UnitProjectLink.objects.filter(projectID=project, unitID=unit).delete()
                    messages.success(request, f'Link between {project} and {unit} removed')
                    return redirect('home-page')
        form = UnitProjectLinkForm()
        context = {
            'all_projects': projects,
            'usersToBeAuthenticated': usersToBeAuthenticated,
            'form': form
        }
        return render(request, 'admin-home.html', context=context)

    projectList = ProjectModel.objects.filter(supervisor1 = request.user)
    return render(request, 'home.html', {'projectList':projectList})


# Project list page
# Including the filter for different education level and units
def project_list(request):
    if request.GET.get('degree'):
        project_filter = request.GET.get('degree')
        projectList1 = ProjectModel.objects.filter(postgraduate=project_filter, draft=False, viewable=1)
        projects = projectList1
    else:
        projectList1 = ProjectModel.objects.filter(draft=False, viewable=1)
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

    context = {
        'all_projects': projects
    }
    return render(request, 'project_list.html', context=context)


# Project details page
def project_detail(request, pk):
    project = ProjectModel.objects.get(pk=pk)
    user = request.user.username
    creator = project.supervisor1.id
    supervisor = Profile.objects.get(user_id=creator)

    strUser = str(user)
    strSupervisor = str(supervisor.user)

    # Check if the project is still a draft, and if so only let the supervisor view it
    if project.draft is True and strUser != strSupervisor:
        return render(request, 'denied.html')
    else:
        prereqs = project.prerequisites.split(",")
        tags = project.projectTags.split(", ")
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
            # Admin fields
            formData.creationDate = datetime.date

            # If the project is saved as a draft, update the project information to match
            if 'Draft' in request.POST:
                formData.draft = 'True'
                formData.save()
                title = form.cleaned_data.get('title')
                messages.success(request, f'Project Proposal Draft {title} was created!')
                return redirect('home-page')
            else:
                formData.draft = 'False'
            formData.submissionDate = timezone.now()
            formData.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'Project Proposal named {title} was submitted!')
            return redirect('home-page')
    else:
        form = ProjectProposalForm()

    return render(request, 'project_registration.html', {'form':form})

# Process for editing a project
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
    if strSupervisor != strUser or project.draft == False:
        if not request.user.is_superuser:
            return render(request, 'denied.html')

    form = EditProject(request.POST or None, request.FILES or None, instance=project)

    if request.method == 'POST':
        if form.is_valid():            
            form.save()
            if 'Draft' in request.POST:
                project.draft = True
                project.save()
                title = form.cleaned_data.get('title')
                messages.success(request, f'Project Proposal Draft {title} was updated!')
                return redirect('home-page')
            else:
                project.draft = False
                project.save()
                title = form.cleaned_data.get('title')

                #Return appropriate message to user
                if request.user.is_superuser:
                    messages.success(request, f'Project Proposal Draft {title} was edited!')
                else:
                    messages.success(request, f'Project Proposal Draft {title} was submitted!')
                return redirect('home-page')
            
    else:
        form = EditProject(instance=project)
    return render(request, 'project-edit.html', context={'form': form})


@login_required(login_url='/login/')
def unit_registration(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = UnitForm(request.POST)
            if form.is_valid():
                formdata = UnitModel()
                formdata.unitCode = form.cleaned_data['unitCode']
                formdata.name = form.cleaned_data['name']
                formdata.description = form.cleaned_data['description']
                formdata.save()
                unitCode = form.cleaned_data['unitCode']
                messages.success(request, f'The unit {unitCode} has been added to the system!')
                return redirect('home-page')
        form = UnitForm()

        return render(request, 'unit_registration.html', context={'form': form})
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
            print(links)
            if links:
                words = ""
                project = str(ProjectModel.objects.values_list('title').get(projectID=pk)[0])
                if len(links) == 1:
                    words = str(UnitModel.objects.values_list('unitCode').get(unitID=links[0].unitID.unitID)[0])
                elif len(links) == 2:
                    words = str(UnitModel.objects.values_list('unitCode').get(unitID=links[0].unitID.unitID)[0])
                    words += " and " + str(UnitModel.objects.values_list('unitCode').get(unitID=links[1].unitID.unitID)[0])
                else:
                    for i in range(len(links) - 2):
                        words += str(UnitModel.objects.values_list('unitCode').get(unitID=links[i].unitID.unitID)[0]) + ", "
                    words += str(UnitModel.objects.values_list('unitCode').get(unitID=links[len(links)-2].unitID.unitID)[0])
                    words += " and " + str(UnitModel.objects.values_list('unitCode').get(unitID=links[len(links)-1].unitID.unitID)[0])
                words += ". Please remove all links before removing projects."
                messages.error(request, f'The project: {project} is still linked with {words}')
            else:
                projectDelete.delete()
                messages.success(request, "Project sucessfully deleted")
    else:
        projectDelete.delete()

    return redirect('home-page')


# 
@login_required(login_url='/login/')
def project_approval(request, pk):
    
    project = get_object_or_404(ProjectModel, projectID=pk) 

    # Check if the user is a superuser or not
    if not request.user.is_superuser or project.draft != False:
        return render(request, 'denied.html')
    elif project.approved == False:
        project.approved = True
        project.save()
    else:
        project.approved = False
        project.viewable = False
        project.save()

    return redirect('home-page')


# 
@login_required(login_url='/login/')
def project_viewable(request, pk):
    
    project = get_object_or_404(ProjectModel, projectID=pk) 

    # Check if the user is a superuser or not
    if not request.user.is_superuser or project.draft != False:
        return render(request, 'denied.html')
    elif project.viewable == False:
        project.viewable = True
        project.save()
    else:
        project.viewable = False
        project.save()

    return redirect('home-page')

# 
@login_required(login_url='/login/')
def project_postgrad(request, pk):
    
    project = get_object_or_404(ProjectModel, projectID=pk) 

    # Check if the user is a superuser or not
    if not request.user.is_superuser or project.draft != False:
        return render(request, 'denied.html')
    elif project.postgraduate == False:
        project.postgraduate = True
        project.save()
    else:
        project.postgraduate = False
        project.save()

    return redirect('home-page')

@login_required(login_url='/login/')
def approve_user(request, pk):
    user = get_object_or_404(User, id=pk)
    if not request.user.is_superuser:
        return render(request, 'denied.html')
    user.is_active = True
    user.save()
    return redirect('home-page')


