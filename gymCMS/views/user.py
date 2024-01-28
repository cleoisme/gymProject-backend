from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, redirect, render
from gymCMS.models.user import User


def list_all_users(request):
    users = User.objects.all()
    users_data = serialize("json", users)

    return render(request, "user_list.html", {"users": users_data})


def show_user_details_by_id(request):
    user_id = request.GET.get("user_id")
    if user_id is not None:
        user = get_object_or_404(User, pk=user_id)
        user_data = serialize("json", user)
        return render(request, "user_details.html", {"user": user_data})
    else:
        return render(request, "NOT_FOUND.html", {"Items Not Found"})


def create_a_user(request):
    new_user = None
    if request.method == "POST":
        new_user = User(request.POST)
        if new_user.is_valid():
            new_user_data = serialize("json", new_user)
            new_user.save()
            return render(request, "user_create.html", {"user": new_user_data})


def update_a_user(request):
    user_id = request.PUT.get("user_id")
    if user_id is not None:
        user = get_object_or_404(User, pk=user_id)
        new_user = User(request.PUT, instance=user)
        if new_user.is_valid():
            new_user.save(user_id)
            return redirect("user_update.html", {"user": new_user})
    else:
        new_user = User(request.PUT)

    return render(request, "NOT_FOUND.html.html", {"Items Not Found"})


def delete_a_user(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        if user_id is not None:
            user = get_object_or_404(User, pk=user_id)
            user.delete()
            return redirect("user_delete.html")

    return render(request, "NOT_FOUND.html.html", {"Items Not Found"})
