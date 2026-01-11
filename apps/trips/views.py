from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Trip, TripBooking


# ================= PUBLIC VIEWS =================

def trip_list(request):
    trips = Trip.objects.all().order_by('-created_at')
    return render(request, 'trips/trip_list.html', {
        'trips': trips
    })


def trip_detail(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    return render(request, 'trips/trip_detail.html', {
        'trip': trip
    })


@login_required
def book_trip(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    TripBooking.objects.create(
        user=request.user,
        trip=trip
    )
    messages.success(request, 'Trip booked successfully!')
    return redirect('accounts:dashboard')


# ================= ADMIN PANEL (SECURED) =================

@login_required
def admin_dashboard(request):
    # 🔐 ADMIN CHECK
    if not request.user.is_staff:
        return redirect('accounts:dashboard')

    return render(request, 'admin_panel/dashboard.html')


@login_required
def admin_trips(request):
    # 🔐 ADMIN CHECK
    if not request.user.is_staff:
        return redirect('accounts:dashboard')

    trips = Trip.objects.all().order_by('-id')
    return render(request, 'admin_panel/trips.html', {
        'trips': trips
    })


@login_required
def add_trip(request):
    # 🔐 ADMIN CHECK
    if not request.user.is_staff:
        return redirect('accounts:dashboard')

    if request.method == 'POST':
        Trip.objects.create(
            title=request.POST.get('title'),
            destination=request.POST.get('destination'),
            duration_days=int(request.POST.get('duration_days')),
            price=request.POST.get('price'),
            created_by=request.user   # 👑 admin user
        )
        messages.success(request, 'Trip added successfully!')
        return redirect('trips:admin_trips')

    return render(request, 'admin_panel/add_trip.html')


@login_required
def edit_trip(request, id):
    # 🔐 ADMIN CHECK
    if not request.user.is_staff:
        return redirect('accounts:dashboard')

    trip = get_object_or_404(Trip, id=id)

    if request.method == 'POST':
        trip.title = request.POST.get('title')
        trip.destination = request.POST.get('destination')
        trip.duration_days = int(request.POST.get('duration_days'))
        trip.price = request.POST.get('price')
        trip.save()

        messages.success(request, 'Trip updated successfully!')
        return redirect('trips:admin_trips')

    return render(request, 'admin_panel/edit_trip.html', {
        'trip': trip
    })


@login_required
def delete_trip(request, id):
    # 🔐 ADMIN CHECK
    if not request.user.is_staff:
        return redirect('accounts:dashboard')

    trip = get_object_or_404(Trip, id=id)
    trip.delete()
    messages.success(request, 'Trip deleted successfully!')
    return redirect('trips:admin_trips')
@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(
        TripBooking,
        id=booking_id,
        user=request.user   
    )

    booking.delete()
    messages.success(request, 'Your trip booking has been cancelled.')
    return redirect('accounts:dashboard')
