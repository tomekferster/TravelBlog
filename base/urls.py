from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('travel_post/<str:pk>/', views.travel_post, name='travel_post'),
]