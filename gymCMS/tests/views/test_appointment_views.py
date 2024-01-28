from django.test import RequestFactory
from django.urls import reverse
from gymCMS.models.appointment import (
    Appointment,
    AppointmentType,
)  # Adjust import based on your actual model structure
from gymCMS.views.appointment import (
    list_all_appointment_types,
    show_appointment_type_details_by_id,
    create_an_appointment_type,
    list_all_appointments,
    show_an_appointment_by_id,
    create_an_appointment,
    update_an_appointment,
    delete_an_appointment,
)


def test_list_all_appointment_types():
    factory = RequestFactory()
    request = factory.get(reverse("list_all_appointment_types"))

    # Assuming you have data in the AppointmentType model for testing
    AppointmentType.objects.create(name="Test Type", duration=30)

    response = list_all_appointment_types(request)
    assert response.status_code == 200
    assert "appointment_type_list.html" in response.template_name
    assert b"Test Type" in response.content


def test_show_appointment_type_details_by_id():
    factory = RequestFactory()
    appointment_type = AppointmentType.objects.create(name="Test Type", duration=30)

    request = factory.get(
        reverse("show_appointment_type_details_by_id"),
        {"appointment_type_id": appointment_type.id},
    )
    response = show_appointment_type_details_by_id(request)

    assert response.status_code == 200
    assert "appointment_type_details.html" in response.template_name
    assert b"Test Type" in response.content


def test_create_an_appointment_type():
    factory = RequestFactory()
    request_data = {
        "name": "New Type",
        "duration": 45,
    }

    request = factory.post(reverse("create_an_appointment_type"), data=request_data)
    response = create_an_appointment_type(request)

    assert response.status_code == 200
    assert "appointment_type_create.html" in response.template_name
    assert b"New Type" in response.content


def test_list_all_appointments():
    factory = RequestFactory()
    request = factory.get(reverse("list_all_appointments"))

    # Assuming you have data in the Appointment model for testing
    Appointment.objects.create(date="2024-01-01", appointment_type_id=1)

    response = list_all_appointments(request)
    assert response.status_code == 200
    assert "appointment_list.html" in response.template_name
    assert b"2024-01-01" in response.content


def test_show_an_appointment_by_id():
    factory = RequestFactory()
    appointment = Appointment.objects.create(date="2024-01-01", appointment_type_id=1)

    request = factory.get(
        reverse("show_an_appointment_by_id"), {"appointment_id": appointment.id}
    )
    response = show_an_appointment_by_id(request)

    assert response.status_code == 200
    assert "appointment_details.html" in response.template_name
    assert b"2024-01-01" in response.content


def test_create_an_appointment():
    factory = RequestFactory()
    request_data = {
        "date": "2024-02-02",
        "appointment_type_id": 2,
    }

    request = factory.post(reverse("create_an_appointment"), data=request_data)
    response = create_an_appointment(request)

    assert response.status_code == 200
    assert "appointment_create.html" in response.template_name
    assert b"2024-02-02" in response.content


def test_update_an_appointment():
    factory = RequestFactory()
    appointment = Appointment.objects.create(date="2024-03-03", appointment_type_id=3)
    request_data = {
        "date": "2024-04-04",
        "appointment_type_id": 4,
    }

    request = factory.put(reverse("update_an_appointment"), data=request_data)
    request.PUT = request_data  # Simulating request.PUT attribute
    request.appointment_id = appointment.id

    response = update_an_appointment(request)

    assert response.status_code == 302  # Redirect status code
    assert "appointment_update.html" in response.url


def test_delete_an_appointment():
    factory = RequestFactory()
    appointment = Appointment.objects.create(date="2024-05-05", appointment_type_id=5)

    request = factory.post(
        reverse("delete_an_appointment"), data={"appointment_id": appointment.id}
    )
    response = delete_an_appointment(request)

    assert response.status_code == 302  # Redirect status code
    assert "appointment_delete.html" in response.url
    assert not Appointment.objects.filter(id=appointment.id).exists()
