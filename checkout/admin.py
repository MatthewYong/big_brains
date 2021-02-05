from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'order_date', 'cart_total',)

    fields = ('order_number', 'profile', 'order_date',
              'first_name', 'last_name',
              'email_address', 'address', 'postcode', 'town',
              'country', 'comments', 'cart_total')

    list_display = ('order_number', 'order_date',
                    'first_name', 'last_name', 'cart_total',)

    ordering = ('-order_date',)


admin.site.register(Order, OrderAdmin)
