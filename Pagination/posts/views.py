from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator

def post(request):
    posts = Post.objects.all()
    paginator = Paginator(posts,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"posts.html",{"posts":page_obj})

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = PostForm()
    return render(request,'forms.html',{'forms':form})