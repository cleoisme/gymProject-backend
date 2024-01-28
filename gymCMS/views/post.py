from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, redirect, render
from gymCMS.models.post import Post


def list_all_posts(request):
    posts = Post.objects.all()
    posts_data = serialize("json", posts)

    return render(request, "post_list.html", {"posts": posts_data})


def show_post_details_by_id(request):
    post_id = request.GET.get("post_id")
    if post_id is not None:
        post = get_object_or_404(Post, pk=post_id)
        post_data = serialize("json", post)
        return render(request, "post_details.html", {"post": post_data})
    else:
        return render(request, "NOT_FOUND.html", {"Items Not Found"})


# Function to create a new post
def create_a_post(request):
    new_post = None
    if request.method == "POST":
        new_post = Post(request.POST)
        if new_post.is_valid():
            new_post_data = serialize("json", new_post)
            new_post.save()
            return render(request, "post_create.html", {"post": new_post_data})


# Function to update an existing post
def update_a_post(request):
    post_id = request.PUT.get("post_id")
    if post_id is not None:
        post = get_object_or_404(Post, pk=post_id)
        new_post = Post(request.POST, instance=post)
        if new_post.is_valid():
            new_post.save()
            return redirect("post_update.html")
        else:
            new_post = Post(instance=post)

    return render(request, "post_update.html", {"post": new_post})


# Function to delete an existing post
def delete_a_post(request):
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        if post_id is not None:
            post = get_object_or_404(Post, pk=post_id)
            post.delete()
            return redirect("post_delete.html")

    return render(request, "NOT_FOUND.html.html", {"Items Not Found"})
