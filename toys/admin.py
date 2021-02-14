from django.contrib import admin
from .models import Toy, Age


class ToyAdmin(admin.ModelAdmin):
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


admin.site.register(Toy, ToyAdmin)
admin.site.register(Age, AgeAdmin)
