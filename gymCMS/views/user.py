from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import User


class UserListView(ListView):
    model = User
    template_name = "user/user_list.html"  # Replace with your actual template


class UserDetailView(DetailView):
    model = User
    template_name = "user/user_detail.html"  # Replace with your actual template


class UserCreateView(CreateView):
    model = User
    template_name = "user/user_form.html"  # Replace with your actual template
    fields = "__all__"


class UserUpdateView(UpdateView):
    model = User
    template_name = "user/user_form.html"  # Replace with your actual template
    fields = "__all__"


class UserDeleteView(DeleteView):
    model = User
    template_name = "user/user_confirm_delete.html"  # Replace with your actual template
    success_url = reverse_lazy("user-list")
