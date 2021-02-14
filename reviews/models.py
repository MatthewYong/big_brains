from django.db import models
from django.contrib.auth.models import User

from toys.models import Toy


class ToyReview(models.Model):

    user_review = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    toy = models.ForeignKey(Toy, related_name='reviews', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=30, null=False, blank=False)
    date = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name
