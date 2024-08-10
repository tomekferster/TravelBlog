from django.contrib import admin
from .models import TravelPost, Comment, Like, Reply, Tag
# Register your models here.

admin.site.register([TravelPost, Comment, Like, Reply, Tag])