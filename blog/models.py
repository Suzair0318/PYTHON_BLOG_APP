from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class BlogModel(models.Model):
    
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    time_stamp = models.DateTimeField(blank=True)
    
    
class BlogComment(models.Model):
    
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogModel , on_delete=models.CASCADE)
    parent = models.ForeignKey('self' , on_delete=models.CASCADE , unique=True )
    timestamp = models.DateTimeField(default=now)