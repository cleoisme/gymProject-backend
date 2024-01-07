from django.db import models
from gymCMS.models.promotion import Promotion
from gymCMS.models.user import User


class AppointmentType(models.Model):
    title = models.CharField(max_length=255)

    def is_valid(self):
        pass


class Appointment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    last_update = models.DateTimeField(auto_now=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    app_type = models.ForeignKey(AppointmentType, on_delete=models.PROTECT)
    trainer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="trainer"
    )
    trainee = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="trainee"
    )
    promotions = models.ManyToManyField(Promotion, null=True)

    def is_valid(self):
        pass
