from django.urls import reverse_lazy
from .models import Notification


def list_all_notifications():
    model = Notification
    template_name = (
        "notification/notification_list.html"  # Replace with your actual template
    )


def show_a_notification():
    model = Notification
    template_name = (
        "notification/notification_detail.html"  # Replace with your actual template
    )


def create_a_notification():
    model = Notification
    template_name = (
        "notification/notification_form.html"  # Replace with your actual template
    )
    fields = "__all__"


def update_a_notification():
    model = Notification
    template_name = (
        "notification/notification_form.html"  # Replace with your actual template
    )
    fields = "__all__"


def delete_a_notification():
    model = Notification
    template_name = "notification/notification_confirm_delete.html"  # Replace with your actual template
    success_url = reverse_lazy("notification-list")
