from django.db import models

from gymCMS.models.user import User


class Post(models.Model):
    subject = models.CharField(max_length=255, default="Default Subject")
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def is_valid(self):
        pass
