from django.shortcuts import render
from .models import Project

def home(request):
    project = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': project})

def all_blogs(request):
    return render(request, 'blog/all_blogs.html')