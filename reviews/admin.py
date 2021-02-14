from django.contrib import admin
from .models import ToyReview


class ToyReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user_review',
        'toy',
        'name',
        'date',
        'comment',
    )


admin.site.register(ToyReview, ToyReviewAdmin)
