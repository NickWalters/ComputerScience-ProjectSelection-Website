from django.http import HttpResponse, Http404
from django.shortcuts import render #template page
from .models import Project #Importing the database model


def index(request):
    all_projects = Project.objects.all()
    context = {'all_projects': all_projects}
    return render(request, 'undergraduate_list/index.html', context)

def detail(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist!")
    return render(request, 'undergraduate_list/detail.html', {'project': project})

