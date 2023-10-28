from . import views
from django.urls import path
from .views import (
    NotificationListView,
    NotificationDetailView,
    NotificationCreateView,
    NotificationUpdateView,
    NotificationDeleteView,
)

# URLConf

urlpatterns = [
    path("hello/", views.check_project),
    path("notifications/", NotificationListView, name="notification-list"),
    path("notifications/<int:pk>/", NotificationDetailView, name="notification-detail"),
    path("notifications/create/", NotificationCreateView, name="notification-create"),
    path(
        "notifications/<int:pk>/update/",
        NotificationUpdateView,
        name="notification-update",
    ),
    path(
        "notifications/<int:pk>/delete/",
        NotificationDeleteView,
        name="notification-delete",
    ),
]
