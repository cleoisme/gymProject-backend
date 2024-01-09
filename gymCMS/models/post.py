from django.db import models

from gymCMS.models.user import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def is_valid(self):
        pass
