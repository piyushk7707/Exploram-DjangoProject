from django.contrib import admin
from .models import Trip, TripBooking


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'destination', 'price', 'duration_days', 'created_at')
    search_fields = ('title', 'destination')


@admin.register(TripBooking)
class TripBookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'trip', 'booked_at')
    list_filter = ('booked_at',)
