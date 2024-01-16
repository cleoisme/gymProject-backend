from django.shortcuts import get_object_or_404, redirect, render
from gymCMS.models.post import Post


def list_all_posts(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", {"posts": posts})


def show_post_details_by_id(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post_details.html", {"post": post})


# Function to create a new post
def create_a_post(request):
    if request.method == "POST":
        # TODO: Parse the payload
        new_post = Post(request.POST)
        if new_post.is_valid():
            new_post.save()
            return redirect(
                "post_list"
            )  # Redirect to the post list view after successful creation
    else:
        new_post = Post()
    return render(request, "post_create.html", {"post": new_post})


# Function to update an existing post
def update_a_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        # TODO: Parse the payload
        new_post = Post(request.POST, instance=post)
        if new_post.is_valid():
            new_post.save()
            return redirect(
                "post_list"
            )  # Redirect to the post list view after successful update
    else:
        new_post = Post(instance=post)
    return render(request, "post_update.html", {"post": new_post})


# Function to delete an existing post
def delete_a_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        post.delete()
        return redirect(
            "post_list"
        )  # Redirect to the post list view after successful deletion
    return render(request, "post_delete.html", {"post": post})
