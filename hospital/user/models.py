# The below code defines Django models for registering doctors and patients with various fields for
# personal and contact information.
from django.db import models

class DoctorReg(models.Model):
    fName = models.CharField(max_length=255)
    lName = models.CharField(max_length=255)
    uId = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)  # Consider using Django's built-in auth system for password handling
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    contact = models.BigIntegerField(unique=True)
    specialist = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fName} {self.lName}"

class PatientReg(models.Model):
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    uId = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Consider using Django's built-in auth system for password handling
    aadhar = models.CharField(max_length=12, unique=True)
    bgroup = models.CharField(max_length=3)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.fName} {self.lName}"