from django.contrib import admin
from .models import TravelPost, Comment, Tag
# Register your models here.

admin.site.register([TravelPost, Comment, Tag])