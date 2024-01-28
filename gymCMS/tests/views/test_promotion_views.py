from django.test import RequestFactory
from django.urls import reverse
from gymCMS.models.promotion import (
    Promotion,
)  # Adjust import based on your actual model structure
from gymCMS.views.promotion import (
    list_all_promotions,
    show_promotion_details_by_id,
    create_a_promotion,
    update_a_promotion,
    delete_a_promotion,
)


def test_list_all_promotions():
    factory = RequestFactory()
    request = factory.get(reverse("list_all_promotions"))

    # Assuming you have data in the Promotion model for testing
    Promotion.objects.create(title="Test Promotion", discount=20)

    response = list_all_promotions(request)
    assert response.status_code == 200
    assert "promotion_list.html" in response.template_name
    assert b"Test Promotion" in response.content


def test_show_promotion_details_by_id():
    factory = RequestFactory()
    promotion = Promotion.objects.create(title="Test Promotion", discount=20)

    request = factory.get(
        reverse("show_promotion_details_by_id"), {"promotion_id": promotion.id}
    )
    response = show_promotion_details_by_id(request)

    assert response.status_code == 200
    assert "promotion_details.html" in response.template_name
    assert b"Test Promotion" in response.content


def test_create_a_promotion():
    factory = RequestFactory()
    request_data = {
        "title": "New Promotion",
        "discount": 15,
    }

    request = factory.post(reverse("create_a_promotion"), data=request_data)
    response = create_a_promotion(request)

    assert response.status_code == 200
    assert "promotion_create.html" in response.template_name
    assert b"New Promotion" in response.content


def test_update_a_promotion():
    factory = RequestFactory()
    promotion = Promotion.objects.create(title="Old Promotion", discount=10)
    request_data = {
        "title": "Updated Promotion",
        "discount": 5,
    }

    request = factory.put(reverse("update_a_promotion"), data=request_data)
    request.PUT = request_data  # Simulating request.PUT attribute
    request.promotion_id = promotion.id

    response = update_a_promotion(request)

    assert response.status_code == 302  # Redirect status code
    assert "promotion_update.html" in response.url


def test_delete_a_promotion():
    factory = RequestFactory()
    promotion = Promotion.objects.create(title="To Be Deleted", discount=30)

    request = factory.post(
        reverse("delete_a_promotion"), data={"promotion_id": promotion.id}
    )
    response = delete_a_promotion(request)

    assert response.status_code == 302  # Redirect status code
    assert "promotion_delete.html" in response.url
    assert not Promotion.objects.filter(id=promotion.id).exists()
