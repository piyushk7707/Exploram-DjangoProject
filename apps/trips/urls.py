from django.urls import path
from . import views

app_name = 'trips'

urlpatterns = [
    # ===== PUBLIC TRIPS =====
    path('', views.trip_list, name='list'),
    path('<int:pk>/', views.trip_detail, name='detail'),
    path('<int:pk>/book/', views.book_trip, name='book'),

    # ===== ADMIN PANEL =====
    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-panel/trips/', views.admin_trips, name='admin_trips'),
    path('admin-panel/trips/add/', views.add_trip, name='add_trip'),
    path('admin-panel/trips/edit/<int:id>/', views.edit_trip, name='edit_trip'),
    path('admin-panel/trips/delete/<int:id>/', views.delete_trip, name='delete_trip'),
    path(
    'cancel-booking/<int:booking_id>/',
    views.cancel_booking,
    name='cancel_booking'
),

]
