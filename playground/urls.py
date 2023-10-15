
from . import views
from django.urls import path

# URLConf
urlpatterns = [
    path("hello/", views.say_hello),
]
