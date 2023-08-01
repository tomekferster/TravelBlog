from django.db import models

# Create your models here.

class TravelPost(models.Model):
    # host = 

    # topic =
    # post_pic =
    name = models.CharField(max_length=200)
    text = models.TextField(max_length=200, null=True, blank=True)
    # commentators =
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
     
