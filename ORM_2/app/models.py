from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Students(models.Model):
    id = models.IntegerField(primary_key=True,serialize=True)
    name = models.CharField(100,null=False )
    age = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(50)],default=18)
    email = models.CharField(50,unique=True,null=False)
    mobile = models.CharField(50,unique=True,null=False)
    
    def __str__(self):
        return self.name