from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('services', views.services, name='services'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('welcome/', views.welcome, name='welcome'),
    path('works/', views.works, name='works'),
]