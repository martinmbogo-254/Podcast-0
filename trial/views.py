from django.shortcuts import render
from .models import Skill, Project
# Create your views here.


def index(request):
    projects= Project.objects.all()
    skills = Skill.objects.all()
    context = {
        'projects': projects,
        'skills': skills
    }

    return render(request, 'trial/home.html', context)
