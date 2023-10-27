from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
