from .views import views
from django.urls import path

# URLConf
urlpatterns = [
    path("api/admins/", views.say_hello),
    path("api/clients/", views.say_hello),
    path("api/appointments/", views.say_hello),
    path("api/notifications/", views.say_hello),
    path("api/posts/", views.say_hello),
]
