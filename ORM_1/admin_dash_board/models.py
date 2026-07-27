from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class User(models.Model):
    id = models.IntegerField(primary_key=True,serialize=True)
    name = models.CharField(255)
    age = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(50)])
    email = models.EmailField(15,unique=True)
    mobile = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name