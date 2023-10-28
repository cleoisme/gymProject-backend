from . import views
from django.urls import path

from .views import (
    # address
    AddressListView,
    AddressDetailView,
    AddressCreateView,
    AddressUpdateView,
    AddressDeleteView,
    # Address Type
    AppointmentTypeListView,
    AppointmentTypeDetailView,
    AppointmentCreateView,
    AppointmentUpdateView,
    AppointmentDeleteView,
    # Post
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    # Pomotion
    PromotionListView,
    PromotionDetailView,
    PromotionCreateView,
    PromotionUpdateView,
    PromotionDeleteView,
    # User
    UserListView,
    UserDetailView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
)

# URLConf

urlpatterns = [
    path("hello/", views.check_project),
    # address
    path("address/", AddressListView, name="address-list"),
    path("address/<int:pk>/", AddressDetailView, name="address-detail"),
    path("address/create/", AddressCreateView, name="address-create"),
    path(
        "address/<int:pk>/update/",
        AddressUpdateView,
        name="address-update",
    ),
    path(
        "address/<int:pk>/delete/",
        AddressDeleteView,
        name="address-delete",
    ),
    # Address Type
    path("addresstype/", AppointmentTypeListView, name="addresstype-list"),
    path("addresstype/<int:pk>/", AppointmentTypeDetailView, name="addresstype-detail"),
    path("addresstype/create/", AppointmentCreateView, name="addresstype-create"),
    path(
        "addresstype/<int:pk>/update/",
        AppointmentUpdateView,
        name="addresstype-update",
    ),
    path(
        "addresstype/<int:pk>/delete/",
        AppointmentDeleteView,
        name="addresstype-delete",
    ),
    # Post
    path("post/", PostListView, name="post-list"),
    path("post/<int:pk>/", PostDetailView, name="post-detail"),
    path("post/create/", PostCreateView, name="post-create"),
    path(
        "post/<int:pk>/update/",
        PostUpdateView,
        name="post-update",
    ),
    path(
        "post/<int:pk>/delete/",
        PostDeleteView,
        name="post-delete",
    ),
    # Pomotion
    path("promotion/", PromotionListView, name="promotion-list"),
    path("promotion/<int:pk>/", PromotionDetailView, name="promotion-detail"),
    path("promotion/create/", PromotionCreateView, name="promotion-create"),
    path(
        "promotion/<int:pk>/update/",
        PromotionUpdateView,
        name="promotion-update",
    ),
    path(
        "promotion/<int:pk>/delete/",
        PromotionDeleteView,
        name="promotion-delete",
    ),
    # User
    path("user/", UserListView, name="user-list"),
    path("user/<int:pk>/", UserDetailView, name="user-detail"),
    path("user/create/", UserCreateView, name="user-create"),
    path(
        "user/<int:pk>/update/",
        UserUpdateView,
        name="user-update",
    ),
    path(
        "user/<int:pk>/delete/",
        UserDeleteView,
        name="user-delete",
    ),
]
