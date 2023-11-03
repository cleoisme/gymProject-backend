from django.http import HttpResponse
from gymCMS.models.address import Address


def list_all_addresses():
    model = Address
    return HttpResponse(str(model))


def show_address_details():
    model = Address
    return HttpResponse(str(model))


def create_an_address():
    model = Address
    return HttpResponse(str(model))


def update_an_address():
    model = Address
    return HttpResponse(str(model))


def delete_an_address():
    model = Address
    return HttpResponse(str(model))
