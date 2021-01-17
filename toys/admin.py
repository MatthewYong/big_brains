from django.contrib import admin
from .models import Toys, Age

class ToysAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'age',
        'price',
        'image',
    )


admin.site.register(Toys)
admin.site.register(Age)
