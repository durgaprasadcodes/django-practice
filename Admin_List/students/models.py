from django.db import models

class Student(models.Model):
    id = models.IntegerField(serialize=True,primary_key=True)
    name = models.CharField(max_length=100,null=False)
    age = models.IntegerField(default=18)
    email = models.CharField(max_length=100,null=False,unique=True)
    
    def __str__(self):
        return self.name