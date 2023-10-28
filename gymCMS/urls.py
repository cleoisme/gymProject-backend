<<<<<<< HEAD
=======
from .views import views
>>>>>>> 4412333 (add views to ./gymCMS)
from django.urls import path
from gymCMS.views.address import (
    create_an_address,
    delete_an_address,
    list_all_addresses,
    show_address_details,
    update_an_address,
)
from gymCMS.views.appointment import (
    create_an_appointment,
    create_an_appointment_type,
    delete_an_appointment,
    list_all_appointment_types,
    list_all_appointments,
    show_an_appointment,
    show_appointment_type_details,
    update_an_appointment,
)
from gymCMS.views.post import (
    create_an_post,
    delete_a_post,
    list_all_posts,
    show_a_post,
    update_a_post,
)

from gymCMS.views.promotion import (
    create_a_promotion,
    delete_a_promotion,
    list_all_promotions,
    show_a_promotion,
    update_a_promotion,
)
from gymCMS.views.user import (
    create_a_user,
    delete_a_user,
    list_all_users,
    show_user_details,
    update_a_user,
)

# URLConf
urlpatterns = [
    # path("hello/", views.check_project),
    # address
    path("addresses/", list_all_addresses, name="address-list"),
    path("addresses/<int:pk>/", show_address_details, name="address-detail"),
    path("address/create/", create_an_address, name="address-create"),
    path(
        "addresses/<int:pk>/update/",
        update_an_address,
        name="address-update",
    ),
    path(
        "addresses/<int:pk>/delete/",
        delete_an_address,
        name="address-delete",
    ),
    # Appointment Type
    path("appointmenttypes/", list_all_appointment_types, name="addresstype-list"),
    path(
        "appointmenttypes/<int:pk>/",
        show_appointment_type_details,
        name="appointmenttype-detail",
    ),
    path(
        "appointmenttype/create/",
        create_an_appointment_type,
        name="appointmenttype-create",
    ),
    # Appointment
    path("appointments/", list_all_appointments, name="appointment-list"),
    path("appointments/<int:pk>/", show_an_appointment, name="appointment-details"),
    path("appointment/create/", create_an_appointment, name="appointment-create"),
    path(
        "appointments/<int:pk>/update/",
        update_an_appointment,
        name="appointment-update",
    ),
    path(
        "appointments/<int:pk>/delete/",
        delete_an_appointment,
        name="appointment-delete",
    ),
    # Post
    path("posts/", list_all_posts, name="post-list"),
    path("posts/<int:pk>/", show_a_post, name="post-detail"),
    path("post/create/", create_an_post, name="post-create"),
    path(
        "posts/<int:pk>/update/",
        update_a_post,
        name="post-update",
    ),
    path(
        "posts/<int:pk>/delete/",
        delete_a_post,
        name="post-delete",
    ),
    # Pomotion
    path("promotions/", list_all_promotions, name="promotion-list"),
    path("promotions/<int:pk>/", show_a_promotion, name="promotion-detail"),
    path("promotion/create/", create_a_promotion, name="promotion-create"),
    path(
        "promotions/<int:pk>/update/",
        update_a_promotion,
        name="promotion-update",
    ),
    path(
        "promotions/<int:pk>/delete/",
        delete_a_promotion,
        name="promotion-delete",
    ),
    # User
    path("users/", list_all_users, name="user-list"),
    path("users/<int:pk>/", show_user_details, name="user-detail"),
    path("user/create/", create_a_user, name="user-create"),
    path(
        "users/<int:pk>/update/",
        update_a_user,
        name="user-update",
    ),
    path(
        "users/<int:pk>/delete/",
        delete_a_user,
        name="user-delete",
    ),
]
