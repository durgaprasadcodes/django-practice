from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Students(models.Model):
    id = models.IntegerField(serialize=True,primary_key=True)
    name = models.CharField(max_length=100,null=True)
    age = models.IntegerField(validators=[MinValueValidator(18),MaxValueValidator(50)],default=18)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.name