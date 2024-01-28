from django.test import RequestFactory
from django.urls import reverse
from gymCMS.models.address import Address

# from yourappname.models import Address  # Import your Address model
from gymCMS.views.address import (
    list_all_addresses,
    show_address_details_by_id,
    create_an_address,
    update_an_address,
    delete_an_address,
)


def test_list_all_addresses():
    factory = RequestFactory()
    request = factory.get(reverse("list_all_addresses"))

    # Assuming you have data in the Address model for testing
    Address.objects.create(street="Test Street", city="Test City", zip_code="12345")

    response = list_all_addresses(request)
    assert response.status_code == 200
    assert "address_list.html" in response.template_name
    assert b"Test Street" in response.content


def test_show_address_details_by_id():
    factory = RequestFactory()
    address = Address.objects.create(
        street="Test Street", city="Test City", zip_code="12345"
    )

    request = factory.get(
        reverse("show_address_details_by_id"), {"address_id": address.id}
    )
    response = show_address_details_by_id(request)

    assert response.status_code == 200
    assert "address_details.html" in response.template_name
    assert b"Test Street" in response.content


def test_create_an_address():
    factory = RequestFactory()
    request_data = {
        "street": "New Street",
        "city": "New City",
        "zip_code": "54321",
    }

    request = factory.post(reverse("create_an_address"), data=request_data)
    response = create_an_address(request)

    assert response.status_code == 200
    assert "address_create.html" in response.template_name
    assert b"New Street" in response.content


def test_update_an_address():
    factory = RequestFactory()
    address = Address.objects.create(
        street="Old Street", city="Old City", zip_code="67890"
    )
    request_data = {
        "street": "Updated Street",
        "city": "Updated City",
        "zip_code": "98765",
    }

    request = factory.put(reverse("update_an_address"), data=request_data)
    request.PUT = request_data  # Simulating request.PUT attribute
    request.address_id = address.id

    response = update_an_address(request)

    assert response.status_code == 302  # Redirect status code
    assert "address_update.html" in response.url


def test_delete_an_address():
    factory = RequestFactory()
    address = Address.objects.create(
        street="To Be Deleted", city="Delete City", zip_code="00000"
    )

    request = factory.post(
        reverse("delete_an_address"), data={"address_id": address.id}
    )
    response = delete_an_address(request)

    assert response.status_code == 302  # Redirect status code
    assert "address_delete.html" in response.url
    assert not Address.objects.filter(id=address.id).exists()
