from django.db import models
from gymCMS.models.user import User


class AppointmentType(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def is_valid(self):
        pass


class Appointment(models.Model):
    subject = models.CharField(max_length=255, null=True)
    description = models.TextField()
    last_update = models.DateTimeField(auto_now=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    appointment_type = models.ForeignKey(
        AppointmentType, on_delete=models.PROTECT, default=1
    )
    trainer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="trainer_appointments"
    )
    trainee = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="trainee_appointments"
    )

    def is_valid(self):
        pass
