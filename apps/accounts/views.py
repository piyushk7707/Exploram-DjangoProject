from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from application.models import TripBooking as Enquiry

from apps.trips.models import Trip, TripBooking

User = get_user_model()


# ================= LOGIN =================
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

           
            if user.is_staff:
                return redirect('trips:admin_dashboard')
            else:
                return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


# ================= SIGNUP =================
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')  

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

           
            if role == 'admin':
                user.is_staff = True  
            else:
                user.is_staff = False  

            user.save()

            messages.success(request, 'Account created successfully! Please login.')
            return redirect('accounts:login')

    return render(request, 'signup.html')


# ================= LOGOUT =================
def user_logout(request):
    logout(request)
    return redirect('accounts:login')


# ================= USER DASHBOARD =================
@login_required(login_url='accounts:login')
def dashboard(request):
    trips = Trip.objects.all()
    my_bookings = TripBooking.objects.filter(
        user=request.user
    ).select_related('trip')
    approved_enquiries = Enquiry.objects.filter(
    email=request.user.email,
    approved=True
)

    return render(
    request,
    'dashboard.html',
    {
        'trips': trips,
        'my_bookings': my_bookings,
        'approved_enquiries': approved_enquiries
    }
    
)


