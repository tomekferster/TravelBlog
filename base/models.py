from django.db import models
from account.models import Account
import uuid
# from sorl.thumbnail import ImageField, get_thumbnail



# class PostPhoto(models.Model):
#     image = ImageField()

#     def save(self, *args, **kwargs):
#         if self.image:
#             self.image = get_thumbnail(self.image, '500x600', quality=99, format='JPEG')
#         super(PostPhoto, self).save(*args, **kwargs)


class TravelPost(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )

    # id = models.UUIDField(default=uuid.uuid4, unique=True,
    #                       primary_key=True, editable=False)   # I might want to use this one for its advantages
    author = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.CharField(default='Travel', max_length=20)
    name = models.CharField(max_length=150)
    text = models.TextField(max_length=2000, null=True, blank=True)
    vote = models.CharField(max_length=200, choices=VOTE_TYPE, null=True, blank=True)
    votes_total = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # image = models.ForeignKey(PostPhoto, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(default='default_post_img.jpg', null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)         # used quotes on Tag, because the Tag class is below the TravelPost class
   
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created']
    
    
class Comment(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(max_length=1000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(TravelPost, on_delete=models.CASCADE) # it is possible to use reply_name = "comments", so instead of using travel_post.comment_set.all (in travel_post.html) it will be possible to use travel_post.comments.all
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.author.username
    
    class Meta:
        ordering = ['-created']


class Like(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Reply(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(max_length=1000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE) # look at the comment for Comment

    def __str__(self):
        return self.author.username
    
    class Meta:
        ordering = ['-created']


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

