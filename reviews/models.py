from django.db import models


class Review(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    comment = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name
