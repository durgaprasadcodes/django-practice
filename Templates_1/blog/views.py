from django.shortcuts import render
from datetime import datetime

class User:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
        
def home(request):
    context = {
        "name":"Durga Prasad Kota",
        "age" :20,
        "skills": ["Python","React","Django","FastAPI","Machine Learning","RAG"],
        "user":User("Durga Prasad",20),
        "blog":{
            "title":"Django Templates Intro",
            "content":"<b>This Is Bold<b>",
            "created_time":datetime(2026,7,20,10,00)
        },
        "emty_value":None
    }
    return render(request,'home.html',context)