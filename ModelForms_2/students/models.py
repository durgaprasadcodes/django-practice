from django.db import models

class Student(models.Model):
    id = models.IntegerField(serialize=True,primary_key=True)
    name = models.CharField(max_length=150,null=False)
    email = models.EmailField(max_length=150,null=False,unique=True)
    