from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


class UserManager(BaseUserManager):
    def create_normal_user(self,name,email,password=None):
        if not email:
            raise ValueError("Email Not Found")
        user = self.model(name=name,email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_super_user(self,email,name,password=None):
        user = self.create_user(name=name,email=email,password=password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user
    
class Users(AbstractUser):
    username = None
    name = models.CharField(max_length=200,null=False)
    email = models.EmailField(max_length=200,null=False,unique=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.name 