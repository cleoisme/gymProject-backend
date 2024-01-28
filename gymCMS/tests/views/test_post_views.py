from django.test import RequestFactory
from django.urls import reverse
from gymCMS.models.post import (
    Post,
)  # Adjust import based on your actual model structure
from gymCMS.views.post import (
    list_all_posts,
    show_post_details_by_id,
    create_a_post,
    update_a_post,
    delete_a_post,
)


def test_list_all_posts():
    factory = RequestFactory()
    request = factory.get(reverse("list_all_posts"))

    # Assuming you have data in the Post model for testing
    Post.objects.create(title="Test Post", content="Test Content")

    response = list_all_posts(request)
    assert response.status_code == 200
    assert "post_list.html" in response.template_name
    assert b"Test Post" in response.content


def test_show_post_details_by_id():
    factory = RequestFactory()
    post = Post.objects.create(title="Test Post", content="Test Content")

    request = factory.get(reverse("show_post_details_by_id"), {"post_id": post.id})
    response = show_post_details_by_id(request)

    assert response.status_code == 200
    assert "post_details.html" in response.template_name
    assert b"Test Post" in response.content


def test_create_a_post():
    factory = RequestFactory()
    request_data = {
        "title": "New Post",
        "content": "New Content",
    }

    request = factory.post(reverse("create_a_post"), data=request_data)
    response = create_a_post(request)

    assert response.status_code == 200
    assert "post_create.html" in response.template_name
    assert b"New Post" in response.content


def test_update_a_post():
    factory = RequestFactory()
    post = Post.objects.create(title="Old Post", content="Old Content")
    request_data = {
        "title": "Updated Post",
        "content": "Updated Content",
    }

    request = factory.put(reverse("update_a_post"), data=request_data)
    request.PUT = request_data  # Simulating request.PUT attribute
    request.post_id = post.id

    response = update_a_post(request)

    assert response.status_code == 302  # Redirect status code
    assert "post_update.html" in response.url


def test_delete_a_post():
    factory = RequestFactory()
    post = Post.objects.create(title="To Be Deleted", content="Delete Content")

    request = factory.post(reverse("delete_a_post"), data={"post_id": post.id})
    response = delete_a_post(request)

    assert response.status_code == 302  # Redirect status code
    assert "post_delete.html" in response.url
    assert not Post.objects.filter(id=post.id).exists()
