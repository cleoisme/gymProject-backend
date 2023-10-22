from django.db import models

# Create your models here.
from django.db import models


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Notification(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)


class User(models.Model):
    is_admin = False
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateTimeField(null=True)
    address = models.OneToOneField(Address, on_delete=models.PROTECT, primary_key=True)


class Client(User):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, "Bronze"),
        (MEMBERSHIP_SILVER, "Silver"),
        (MEMBERSHIP_GOLD, "Gold"),
    ]

    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE
    )


class Admin(User):
    is_admin = True
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Trainer(User):
    pass


class AppointmentType(models.Model):
    title = models.CharField(max_length=255)


class Appointment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    last_update = models.DateTimeField(auto_now=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    app_type = models.ForeignKey(AppointmentType, on_delete=models.PROTECT)
    trainer = models.OneToOneField(Trainer, on_delete=models.SET_NULL)
    promotions = models.ManyToManyField(Promotion, null=True)


# Task


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
