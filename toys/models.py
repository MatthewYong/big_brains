from django.db import models


class Age(models.model):
    name = models.CharField(max_length=200)
    frontend_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
