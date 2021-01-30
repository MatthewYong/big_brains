from django.db import models


class Order(models.Model):

    order_number = models.Charfield(max_length=40, null=False, editable=False)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    email_address = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    postcode = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    procurement_date = models.DateTimeField(auto_now_add=True)
    cart_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
