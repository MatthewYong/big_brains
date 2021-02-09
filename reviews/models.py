from django.db import models
from toys.models import Toy


class Review(models.Model):
    toy_review_id = models.ForeignKey(Toy, default=None,
                                      on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=False, blank=False)
    date = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name
