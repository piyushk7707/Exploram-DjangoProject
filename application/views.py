from django.shortcuts import render, redirect # type: ignore
from application.models import*
from .models import Contact
from django.contrib import messages # type: ignore
from .forms import TripBookingForm
from django.contrib.auth import authenticate, login
from .forms import ContactForm
from .models import ContactSubmission
from django.contrib.auth.decorators import login_required
from .models import Contact, TripBooking

# Create your views here.
def home(request):
    return render(request,'index.html')




def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})



def Services(request):
    if request.method == 'POST':
        form = TripBookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your trip has been booked successfully!')
            return redirect('/Services/#book-trip')  # Redirect after POST
    else:
        form = TripBookingForm()
    
    return render(request, 'Services.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def dashboard(request):
    submissions = ContactSubmission.objects.all()
    return render(request, 'dashboard.html', {'submissions': submissions})


def dashboard(request):
    # Fetch all entries from database
    contact_submissions = Contact.objects.all()
    trip_bookings = TripBooking.objects.all()

    context = {
        'contact_submissions': contact_submissions,
        'trip_bookings': trip_bookings,
    }
    return render(request, 'dashboard.html', context)

