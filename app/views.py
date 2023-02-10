from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def resume(request):
    return render(request, 'resume.html')


def services(request):
    return render(request, 'services.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def welcome(request):
    return render(request, 'welcome.html')


def works(request):
    return render(request, 'works.html')
