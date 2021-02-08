from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Blog(models.Model):
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False, blank=False)
    author_friendly = models.CharField(max_length=30, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    date = models.DateTimeField(default=timezone.now)
    article = models.CharField(max_length=10000, null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.title
