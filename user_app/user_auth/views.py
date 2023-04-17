from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Patient, Doctor


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.address_line1 = form.cleaned_data.get('address_line1')
            user.city = form.cleaned_data.get('city')
            user.state = form.cleaned_data.get('state')
            user.pincode = form.cleaned_data.get('pincode')
            user.profile_picture = request.FILES.get('profile_picture')
            user.save()
            if form.cleaned_data.get('is_doctor'):
                Doctor.objects.create(user=user)
            else:
                Patient.objects.create(user=user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, 'doctor'):
                return redirect('doctor_dashboard')
            else:
                return redirect('patient_dashboard')
    return render(request, 'login.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html', {'user': request.user})


@login_required
def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html', {'user': request.user})
