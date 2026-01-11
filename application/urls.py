from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('Services/', views.Services, name='Services'),
    path('ai-planner/', views.ai_planner, name='ai_planner'),

]
