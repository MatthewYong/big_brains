from django.db import models


class Age(models.Model):

    class Meta:
        verbose_name_plural = 'Age'

    name = models.CharField(max_length=200)
    frontend_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_frontend_name(self):
        return self.frontend_name


class Toy(models.Model):

    class Meta:
        verbose_name_plural = 'Toys'

    age = models.ForeignKey('Age', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class ToyReview(models.Model):

    toy_review = models.ForeignKey('Toy', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=30, null=False, blank=False)
    date = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name
