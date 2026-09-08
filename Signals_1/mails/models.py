from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    name = models.CharField(max_length=200,null=False)
    email = models.EmailField(max_length=200,unique=True,null=False)
    created_at = models.DateField(auto_now_add=True)
    
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = [] 
    
