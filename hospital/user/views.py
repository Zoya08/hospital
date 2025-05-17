from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import DoctorReg, PatientReg

# Home Page
def index(request):
    return render(request, 'index.html')

# Home2 Page
def home2(request):
    return render(request, 'home2.html')


# About Page
def about(request):
    return render(request, 'about.html')

# Service Page
def service(request):
    return render(request, 'service.html')

# Doctor Login
from django.contrib.auth import authenticate, login

def doctor_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        doctor = DoctorReg.objects.filter(email=email).first()
        
        if doctor and doctor.password == password:  # Direct password comparison
            request.session['email'] = email
            request.session['is_doctor'] = True
            messages.success(request, 'Successfully logged in!')
            return redirect('home')  # Ensure 'home' is properly defined in urls.py
        else:
            messages.error(request, 'Invalid email or password!')
            return redirect('doctor_login')
            
    return render(request, 'doctor_login.html', {'title': 'Login'})

# Doctor Registration
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
            messages.error(request, 'All fields are required!')
            return redirect('doctor_register')

        if DoctorReg.objects.filter(email=email).exists():
            messages.error(request, 'Doctor with this email already exists!')
            return redirect('doctor_register')

        try:
            DoctorReg.objects.create(
                fName=fName, lName=lName, uId=uId, email=email,
                password=make_password(password),  # Hash password
                state=state, city=city, gender=gender, contact=contact, specialist=specialist
            )
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('doctor_login')
        except Exception as e:
            messages.error(request, f"Registration error: {e}")
            return redirect('doctor_register')
    return render(request, 'doctor_register.html', {'title': 'Doctor Register'})

# Patient Login
def patient_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        patient = PatientReg.objects.filter(email=email).first()

        if patient and patient.password == password:  # Direct password comparison
            request.session['email'] = email
            messages.success(request, 'Successfully logged in!')
            return redirect('home2')
        else:
            messages.error(request, 'Invalid credentials, please try again.')
            return redirect('patient_login')

    return render(request, 'patient_login.html', {'title': 'Patient Login'})

# Patient Registration
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
            messages.error(request, 'All fields are required!')
            return redirect('patient_register')

        if PatientReg.objects.filter(email=email).exists() or PatientReg.objects.filter(aadhar=aadhar).exists():
            messages.error(request, 'Patient with this email or Aadhar already exists!')
            return redirect('patient_register')

        try:
            PatientReg.objects.create(
                fName=fName, lName=lName, uId=uId, email=email,
                password=make_password(password),  # Hash password
                aadhar=aadhar, bgroup=bgroup, gender=gender, dob=dob, age=age,
                state=state, city=city, contact=contact, address=address
            )
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('patient_login')
        except Exception as e:
            messages.error(request, f"Registration error: {e}")
            return redirect('patient_register')
    return render(request, 'patient_register.html', {'title': 'Patient Register'})

# Home Page with User Session
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

# Logout Function
def logout(request):
    request.session.flush()  # Clears session data
    messages.success(request, 'Successfully logged out!')
    return redirect('index')

