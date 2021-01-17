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

    ordering = ('name',)


class AgeAdmin(admin.ModelAdmin):
    list_display = (
        'frontend_name',
    )


admin.site.register(Toys, ToysAdmin)
admin.site.register(Age, AgeAdmin)
