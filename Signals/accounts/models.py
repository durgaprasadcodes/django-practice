from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,name,email,password=None):
        user = self.model(email=self.normalize_email(email),name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_super_user(self,name,email,password=None):
        user = self.create_user(name=name,email=email,password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    name = models.CharField(max_length=200,null=False)
    email = models.EmailField(max_length=200,unique=True,null=False)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self): 
        return self.email