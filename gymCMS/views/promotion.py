from django.http import HttpResponse
from playground.models import Promotion


def list_all_promotions():
    model = Promotion
    return HttpResponse(str(model))


def show_a_promotion():
    model = Promotion
    return HttpResponse(str(model))


def create_a_promotion():
    model = Promotion
    return HttpResponse(str(model))


def update_a_promotion():
    model = Promotion
    return HttpResponse(str(model))


def delete_a_promotion():
    model = Promotion
    return HttpResponse(str(model))
