from django.urls import reverse_lazy

from gymCMS.models.post import Post


def list_all_posts():
    model = Post
    template_name = "post/post_list.html"  # Replace with your actual template


def show_a_post():
    model = Post
    template_name = "post/post_detail.html"  # Replace with your actual template


def create_an_post():
    model = Post
    template_name = "post/post_form.html"  # Replace with your actual template
    fields = "__all__"


def update_a_post():
    model = Post
    template_name = "post/post_form.html"  # Replace with your actual template
    fields = "__all__"


def delete_a_post():
    model = Post
    template_name = "post/post_confirm_delete.html"  # Replace with your actual template
    success_url = reverse_lazy("post-list")
