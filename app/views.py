from django.core.mail import send_mail
from django.shortcuts import render
from .models import Skill, Experience, Education, RepoType, Repo, Team


def home(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        msg = request.POST.get('message')
        email = request.POST.get('email')
        message = f"Full name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {msg}"
        send_mail(
            name, message, email,
            ['abduqulovabdulla3108@gmail.com']
        )
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


def teams(request):
    teams = Team.objects.all()
    ctx = {'teams': teams}
    return render(request, 'team.html', ctx)


def welcome(request):
    return render(request, 'welcome.html')


def works(request):
    repo_types = RepoType.objects.all()
    repos = Repo.objects.all()
    ctx = {'repo_types': repo_types,
           'repos': repos,
           }
    return render(request, 'works.html', ctx)
