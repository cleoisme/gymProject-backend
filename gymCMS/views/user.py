from django.urls import reverse_lazy
from gymCMS.models.user import User


def list_all_users():
    model = User
    template_name = "user/user_list.html"  # Replace with your actual template


def show_user_details():
    model = User
    template_name = "user/user_detail.html"  # Replace with your actual template


def create_a_user():
    model = User
    template_name = "user/user_form.html"  # Replace with your actual template
    fields = "__all__"


def update_a_user():
    model = User
    template_name = "user/user_form.html"  # Replace with your actual template
    fields = "__all__"


def delete_a_user():
    model = User
    template_name = "user/user_confirm_delete.html"  # Replace with your actual template
    success_url = reverse_lazy("user-list")
