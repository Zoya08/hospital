
from django.shortcuts import render,redirect
"""
    The above code consists of views for a Django web application that handles doctor and patient
    registration, login, and logout functionalities.
    
    :param request: The `request` parameter in Django views represents the HTTP request that was sent to
    the server. It contains information about the request, such as the user's session data, any data
    sent in the request (POST or GET parameters), and more. The view functions use the `request` object
    to access
    :return: The views in the code are returning either a rendered HTML template or redirecting to a
    specific URL. The `render` function is used to render an HTML template with the provided context
    data, while the `redirect` function is used to redirect the user to a different URL.
    """
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def doctor_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        doctor = DoctorReg.objects.filter(email=email).first()
        if doctor and doctor.password == password:  # Note: This is not secure, use Django's auth system instead
            request.session['email'] = email
            request.session['is_doctor'] = True
            messages.success(request, 'Successfully Login!!')
            return redirect('home')
        else:
            messages.error(request, 'Please enter correct credentials!')
            return redirect('doctor_login')
    else:
        return render(request, 'doctor_login.html', {'title': 'login'})

def doctor_register(request):
    if request.method == 'POST':
        fName = request.POST.get('fName')
        lName = request.POST.get('lName')
        uId = request.POST.get('uId')
        email = request.POST.get('email')
        password = request.POST.get('password')
        state = request.POST.get('state')
        city = request.POST.get('city')
        gender = request.POST.get('gender')
        contact = request.POST.get('contact')
        specialist = request.POST.get('specialist')

        if not all([fName, lName, uId, email, password, state, city, gender, contact, specialist]):
            messages.error(request, 'Please fill out all fields!')
            return redirect('doctor_register')

        if DoctorReg.objects.filter(email=email).exists():
            messages.error(request, 'Doctor already registered with this email!')
            return redirect('doctor_register')

        try:
            DoctorReg.objects.create(
                fName=fName,
                lName=lName,
                uId=uId,
                email=email,
                password=password,
                state=state,
                city=city,
                gender=gender,
                contact=contact,
                specialist=specialist
            )
            messages.success(request, 'Successfully Registered!!')
            return redirect('doctor_login')
        except Exception as e:
            messages.error(request, f"Error during registration: {e}")
            return redirect('doctor_register')
    else:
        return render(request, 'doctor_register.html', {'title': 'Register'})

def patient_login(request):
    if request.method == 'POST':
        password = request.POST['password']
        email = request.POST['email']
        patient = PatientReg.objects.filter(password=password, email=email).first()
        if patient is not None:
            request.session['email'] = email
            messages.success(request, 'Successfully Login!!')
            return redirect('home')
        else:
            messages.error(request, 'Please enter correct credentials!')
            return redirect('patient_login')
    else:
        return render(request, 'patient_login.html', {'title': 'login'})

def patient_register(request):
    if request.method == 'POST':
        fName = request.POST.get('fName')
        lName = request.POST.get('lName')
        uId = request.POST.get('uId')
        email = request.POST.get('email')
        aadhar = request.POST.get('aadhar')
        bgroup = request.POST.get('bgroup')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        state = request.POST.get('state')
        city = request.POST.get('city')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        address = request.POST.get('address')

        if not all([fName, lName, uId, email, aadhar, bgroup, dob, age, password, state, city, gender, contact, address]):
            messages.error(request, 'Please fill out all fields!')
            return redirect('patient_register')

        if PatientReg.objects.filter(email=email).exists() or PatientReg.objects.filter(aadhar=aadhar).exists():
            messages.error(request, 'Patient already registered with this email or aadhar!')
            return redirect('patient_register')

        try:
            PatientReg.objects.create(
                fName=fName,
                lName=lName,
                uId=uId,
                email=email,
                password=password,
                aadhar=aadhar,
                bgroup=bgroup,
                gender=gender,
                dob=dob,
                age=age,
                state=state,
                city=city,
                contact=contact,
                address=address
            )
            messages.success(request, 'Successfully Registered!!')
            return redirect('patient_login')
        except Exception as e:
            messages.error(request, f"Error during registration: {e}")
            return redirect('patient_register')
    else:
        return render(request, 'patient_register.html', {'title': 'Register'})

@login_required
def home(request):
    user_name = ""
    if 'email' in request.session:
        doctor = DoctorReg.objects.filter(email=request.session['email']).first()
        if doctor:
            user_name = doctor.fName
        else:
            patient = PatientReg.objects.filter(email=request.session['email']).first()
            if patient:
                user_name = patient.fName
    
    return render(request, 'home.html', {'user_name': user_name})

    

def logout(request):
    if 'email' in request.session:
        del request.session['email']
    if 'is_doctor' in request.session:
        del request.session['is_doctor']
    messages.success(request, 'Successfully logged out!')
    return redirect('/')



