import uuid

from django.db.models import Sum
from django.db import models
from django_countries.fields import CountryField

from toys.models import Toy
from profiles.models import Profile


class Order(models.Model):

    order_number = models.CharField(max_length=40, null=False, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                                null=True, blank=True, related_name='orders')
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    email_address = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town = models.CharField(max_length=50, null=False, blank=False)
    country = CountryField(blank_label='Country', null=False, blank=False)
    comments = models.CharField(max_length=1000, null=True, blank=True)
    order_date = models.DateField("Order Date", auto_now_add=True)
    cart_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Function that generates a unique order number.
        Code used from CI checkout lesson
        """
        return uuid.uuid4().hex.upper()

    def update_cart_total(self):
        """Updates cart total each time an order item is added.
        Code partly used from CI checkout lesson"""
        self.cart_total = self.lineitems.aggregate(
                            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already. Code used from CI checkout lesson
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


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

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already. Code used from CI checkout lesson
        """
        self.lineitem_total = self.toy.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.toy.sku} on order {self.order.order_number}'
