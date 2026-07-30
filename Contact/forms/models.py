from django.db import models

class Contact(models.Model):
    id = models.IntegerField(serialize=True,primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    created_at =models.DateTimeField(auto_now_add=True)
    
    def __str__(self): 
        return self.name