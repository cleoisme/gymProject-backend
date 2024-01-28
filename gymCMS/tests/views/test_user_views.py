from django.test import RequestFactory
from django.urls import reverse
from gymCMS.models.user import (
    User,
)  # Adjust import based on your actual model structure
from gymCMS.views.user import (
    list_all_users,
    show_user_details_by_id,
    create_a_user,
    update_a_user,
    delete_a_user,
)


def test_list_all_users():
    factory = RequestFactory()
    request = factory.get(reverse("list_all_users"))

    # Assuming you have data in the User model for testing
    User.objects.create(username="TestUser", email="test@example.com")

    response = list_all_users(request)
    assert response.status_code == 200
    assert "user_list.html" in response.template_name
    assert b"TestUser" in response.content


def test_show_user_details_by_id():
    factory = RequestFactory()
    user = User.objects.create(username="TestUser", email="test@example.com")

    request = factory.get(reverse("show_user_details_by_id"), {"user_id": user.id})
    response = show_user_details_by_id(request)

    assert response.status_code == 200
    assert "user_details.html" in response.template_name
    assert b"TestUser" in response.content


def test_create_a_user():
    factory = RequestFactory()
    request_data = {
        "username": "NewUser",
        "email": "newuser@example.com",
    }

    request = factory.post(reverse("create_a_user"), data=request_data)
    response = create_a_user(request)

    assert response.status_code == 200
    assert "user_create.html" in response.template_name
    assert b"NewUser" in response.content


def test_update_a_user():
    factory = RequestFactory()
    user = User.objects.create(username="OldUser", email="olduser@example.com")
    request_data = {
        "username": "UpdatedUser",
        "email": "updateduser@example.com",
    }

    request = factory.put(reverse("update_a_user"), data=request_data)
    request.PUT = request_data  # Simulating request.PUT attribute
    request.user_id = user.id

    response = update_a_user(request)

    assert response.status_code == 302  # Redirect status code
    assert "user_update.html" in response.url


def test_delete_a_user():
    factory = RequestFactory()
    user = User.objects.create(username="ToBeDeleted", email="tobedeleted@example.com")

    request = factory.post(reverse("delete_a_user"), data={"user_id": user.id})
    response = delete_a_user(request)

    assert response.status_code == 302  # Redirect status code
    assert "user_delete.html" in response.url
    assert not User.objects.filter(id=user.id).exists()
