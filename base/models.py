from django.db import models
import uuid
# Create your models here.

   
class TravelPost(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, unique=True,
    #                       primary_key=True, editable=False)   # I might want to use this one for its advantages
    # author = 
    # topic =
    # commentators =
    name = models.CharField(max_length=200)
    text = models.TextField(max_length=200, null=True, blank=True)
    votes_total = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='default_post_img.jpg', null=True, blank=True)
    tags = models.ManyToManyField('Tag', null=True, blank=True)         # used quotes on Tag, because the Tag class is below the TravelPost class
   
    def __str__(self):
        return self.name
    
    
class Comment(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    # author =
    text = models.TextField(max_length=200, null=True, blank=True)
    vote_post = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(TravelPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.vote_post
    

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

