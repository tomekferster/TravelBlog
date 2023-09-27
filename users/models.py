from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(default='profile_pictures/default_profile_img.jpg', null=True, blank=True, upload_to='profile_pictures/')
    created = models.DateTimeField(auto_now_add=True)
    social_instagram = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.user.username

