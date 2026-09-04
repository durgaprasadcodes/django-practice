from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"


class PostCreateView(CreateView):
    model = Post
    template_name = "post_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("post_list")


class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_form.html"
    fields = ["title", "content"]
    context_object_name = "post"
    success_url = reverse_lazy("post_list")


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")