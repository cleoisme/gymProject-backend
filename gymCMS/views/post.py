from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "post/post_list.html"  # Replace with your actual template


class PostDetailView(DetailView):
    model = Post
    template_name = "post/post_detail.html"  # Replace with your actual template


class PostCreateView(CreateView):
    model = Post
    template_name = "post/post_form.html"  # Replace with your actual template
    fields = "__all__"


class PostUpdateView(UpdateView):
    model = Post
    template_name = "post/post_form.html"  # Replace with your actual template
    fields = "__all__"


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post/post_confirm_delete.html"  # Replace with your actual template
    success_url = reverse_lazy("post-list")
