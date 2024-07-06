# This code snippet is defining URL patterns for a Django web application. Each `path` function call
# maps a URL pattern to a specific view function. Here's a breakdown of what each line does:
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('doctor_login/', views.doctor_login, name='doctor_login'),
    path('doctor_register/', views.doctor_register, name='doctor_register'),
    path('patient_login/', views.patient_login, name='patient_login'),
    path('patient_register/', views.patient_register, name='patient_register'),
    path('logout/', views.logout, name='logout'),
]
