from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Registers(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE) 
    # _id = models.IntegerField()
    # username = models.CharField(max_length=25)
    # email = models.EmailField(max_length=25)
    # password = models.CharField(max_length=25)
class Login(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Posts(models.Model):
    # fields of the model
    title = models.CharField(max_length=255)
    description = models.TextField()
    # rename the instances of model
    # with their title name
    
    def __str__(self):
        return self.title
     