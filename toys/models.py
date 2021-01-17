from django.db import models


class Age(models.model):
    name = models.CharField(max_length=200)
    frontend_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_frontend_name(self):
        return self.frontend_name


class Toys(models.model):
    age = models.ForeignKey('Age', null=True, blank=True, ondelete=models.SET_NULL)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name