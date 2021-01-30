import uuid
from django.db.models import Sum
from django.conf import settings
from django.db import models
from django_countries.fields import CountryField

from toys.models import Toy


class Order(models.Model):

    order_number = models.Charfield(max_length=40, null=False, editable=False)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    email_address = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town = models.CharField(max_length=50, null=False, blank=False)
    country = CountryField(multiple=True)
    procurement_date = models.DateTimeField(auto_now_add=True)
    cart_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def generate_order_number(self):
        """
        Function that generates a unique order number
        """
        return uuid.uuid4().hex.upper()


class OrderLineItem(models.Model):
    order = models.ForeignKey(
                            Order, null=False, blank=False,
                            on_delete=models.CASCADE, related_name='lineitems')
    toy = models.ForeignKey(
                        Toy, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
                                max_digits=6, decimal_places=2, null=False,
                                blank=False, editable=False)
