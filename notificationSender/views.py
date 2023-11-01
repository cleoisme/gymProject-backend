from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Notification


# Create your views here.
def check_project(request):
    return HttpResponse("This is the Notification Sender Project!")


class NotificationListView(ListView):
    model = Notification
    template_name = (
        "notification/notification_list.html"  # Replace with your actual template
    )


class NotificationDetailView(DetailView):
    model = Notification
    template_name = (
        "notification/notification_detail.html"  # Replace with your actual template
    )


class NotificationCreateView(CreateView):
    model = Notification
    template_name = (
        "notification/notification_form.html"  # Replace with your actual template
    )
    fields = "__all__"


class NotificationUpdateView(UpdateView):
    model = Notification
    template_name = (
        "notification/notification_form.html"  # Replace with your actual template
    )
    fields = "__all__"


class NotificationDeleteView(DeleteView):
    model = Notification
    template_name = "notification/notification_confirm_delete.html"  # Replace with your actual template
    success_url = reverse_lazy("notification-list")
