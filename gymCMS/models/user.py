from django.db import models

from gymCMS.models.address import Address


class User(models.Model):
<<<<<<< HEAD
    is_admin = models.BooleanField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=128)  # This is the password field
=======
    is_admin = False
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
>>>>>>> 0f70e3a (break classess)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateTimeField(null=True)
    address = models.OneToOneField(Address, on_delete=models.PROTECT, primary_key=True)

<<<<<<< HEAD
=======

class Client(User):
>>>>>>> 0f70e3a (break classess)
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
<<<<<<< HEAD
=======


class Admin(User):
    is_admin = True
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
>>>>>>> 0f70e3a (break classess)
