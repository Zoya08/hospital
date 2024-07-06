# This code snippet is from a Django project's admin.py file.
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(DoctorReg)
admin.site.register(PatientReg)