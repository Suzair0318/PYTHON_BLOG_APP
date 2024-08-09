from django.db import models

# Create your models here.


    

class ContactModel(models.Model):
    
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    complain = models.TextField()
    
