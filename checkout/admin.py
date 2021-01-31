from django.contrib import admin
from .models import Order, OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date', 'delivery_cost',
                       'order_total',)

    fields = ('order_number', 'date', 'first_name', 'last_name', 'email',
              'address', 'postcode', 'town', 'country',)
