from django.urls import path
from .views import (
    create_a_notification,
    delete_a_notification,
    list_all_notifications,
    show_a_notification,
    update_a_notification,
)

# URLConf

urlpatterns = [
    path("notifications/", list_all_notifications, name="notification-list"),
    path("notifications/<int:pk>/", show_a_notification, name="notification-detail"),
    path("notifications/create/", create_a_notification, name="notification-create"),
    path(
        "notifications/<int:pk>/update/",
        update_a_notification,
        name="notification-update",
    ),
    path(
        "notifications/<int:pk>/delete/",
        delete_a_notification,
        name="notification-delete",
    ),
]
