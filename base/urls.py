from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('travel-post/<str:pk>/', views.travel_post, name='travel-post'),
    path('create-travel-post/', views.create_travel_post, name='create-travel-post'),
    path('contact/', views.contact, name='contact'),
]