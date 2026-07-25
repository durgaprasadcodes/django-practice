from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Student(models.Model):
    name = models.CharField(max_length=100,null=False)
    age = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(30)]
    )
    email = models.EmailField(unique=True,null=False)
    enrollment_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name