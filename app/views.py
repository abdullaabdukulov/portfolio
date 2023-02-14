from django.shortcuts import render
from .models import Skill, Experience, Education


def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    skills = Skill.objects.all()
    return render(request, 'about.html', {'skills': skills})


def resume(request):
    experiences = Experience.objects.all().order_by('-created_at')
    educations = Education.objects.all().order_by('-created_at')
    ctx = {'experiences': experiences,
           'educations': educations}

    return render(request, 'resume.html', ctx)


def services(request):
    return render(request, 'services.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def welcome(request):
    return render(request, 'welcome.html')


def works(request):
    return render(request, 'works.html')
