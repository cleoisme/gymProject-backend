from django.http import HttpResponse
from gymCMS.models.appointment import Appointment, AppointmentType


def list_all_appointment_types():
    model = AppointmentType
    return HttpResponse(str(model))


def show_appointment_type_details():
    model = AppointmentType
    return HttpResponse(str(model))


def create_an_appointment_type():
    model = AppointmentType
    return HttpResponse(str(model))


def list_all_appointments():
    model = Appointment
    return HttpResponse(str(model))


def show_an_appointment():
    model = Appointment
    return HttpResponse(str(model))


def create_an_appointment():
    model = Appointment
    return HttpResponse(str(model))


def update_an_appointment():
    model = Appointment
    return HttpResponse(str(model))


def delete_an_appointment():
    model = Appointment
    return HttpResponse(str(model))
