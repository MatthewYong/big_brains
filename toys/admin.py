from django.contrib import admin
from .models import Toy, Age, ToyReview


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


class ToyReviewAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date',
        'comment',
    )


admin.site.register(Toy, ToyAdmin)
admin.site.register(Age, AgeAdmin)
admin.site.register(ToyReview, ToyReviewAdmin)
