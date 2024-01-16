from django.shortcuts import get_object_or_404, redirect, render
from gymCMS.models.user import User


def list_all_users(request):
    users = User.objects.all()
    return render(request, "user_list.html", {"users": users})


def show_user_details_by_id(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, "user_details.html", {"user": user})


def create_a_user(request):
    if request.method == "POST":
        new_user = User(request.POST)
        if new_user.is_valid():
            new_user.save()
            return redirect(
                "user_details", user_id=new_user.pk
            )  # Redirect to user details page after creation
    else:
        new_user = User()
    return render(request, "user_create.html", {"user": new_user})


def update_a_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        new_user = User(request.POST, instance=user)
        if new_user.is_valid():
            new_user.save()
            return redirect(
                "user_details", user_id=new_user.pk
            )  # Redirect to user details page after update
    else:
        new_user = User(instance=user)
    return render(request, "user_update.html", {"user": new_user})


def delete_a_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        user.delete()
        return redirect("list_all_users")  # Redirect to user list after deletion
    return render(request, "user_delete.html", {"user": user})
