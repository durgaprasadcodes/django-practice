from django.db import models

class Student(models.Model):
    id = models.IntegerField(serialize=True,primary_key=True)
    name = models.CharField(max_length=150,null=False)
    age = models.IntegerField()
    email = models.EmailField(max_length=150,unique=True,null=False)
    
    def __str__(self):
        return self.name