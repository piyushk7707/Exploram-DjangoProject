from django.contrib import admin
from django.urls import path
from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('Services/', views.Services, name='Services'), 
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    
]
