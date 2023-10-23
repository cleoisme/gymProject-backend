from django.db import models


# Create your models here.
class Notification(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
