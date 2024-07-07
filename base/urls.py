from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('travel-post/<str:pk>/', views.travel_post, name='travel-post'),
    path('create-travel-post/', views.create_travel_post, name='create-travel-post'),
    path('update-travel-post/<str:pk>/', views.update_travel_post, name='update-travel-post'),
    path('delete-travel-post/<str:pk>/', views.delete_travel_post, name='delete-travel-post'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]