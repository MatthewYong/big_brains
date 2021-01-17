from django.contrib import admin
from .models import Toys, Age


class ToysAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age',
        'price',
        'image',
    )


class AgeAdmin(admin.ModelAdmin):
    list_display = (
        'frontend_name',
    )

admin.site.register(Toys)
admin.site.register(Age)
