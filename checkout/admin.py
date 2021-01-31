from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total')


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'order_date', 'delivery_cost',
                       'order_total',)

    fields = ('order_number', 'order_date', 'first_name', 'last_name', 'email',
              'address', 'postcode', 'town', 'country',)

    list_display = ('order_number', 'order_date', 'first_name', 'last_name',
                    'order_total',)

    ordering = ('-order_date')


admin.site.register(Order, OrderAdmin)
