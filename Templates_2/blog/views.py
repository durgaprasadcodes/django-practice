from django.shortcuts import render
from datetime import datetime

def home(request):
    post = {
        "title" : "My Secnd Templates Post",
        "description" : "Django is a high level Python web frameworks",
        "author":None,
        "created_at":datetime(2026,7,21,10,6),
        "comments_count" : 5,
        "tags" : ["Django","Python","Web Development"],
        "price":1000
    }
    return render(request,"blog.html",{"post":post})