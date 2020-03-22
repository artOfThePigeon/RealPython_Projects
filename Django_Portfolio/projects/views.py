from django.shortcuts import render
from projects.models import Project


# Create your views here.
def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'all_projects.html', {'projects': projects})

def project_list(request):
    return render(request, 'projects/index.html')
