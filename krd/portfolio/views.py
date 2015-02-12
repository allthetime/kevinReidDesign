from django.shortcuts import render
from portfolio.models import Project, Image, Biography


from django.shortcuts import get_object_or_404, render

def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

def project(request,path):
    project = Project.objects.get(path=path)
    images = Image.objects.filter(project=project.id)
    return render(request, 'project_page.html', {'images':images, 'project':project})

# Create your views here.
