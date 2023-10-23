from . import views
from django.urls import path

# URLConf
urlpatterns = [
    path("hello/", views.check_project),
]
