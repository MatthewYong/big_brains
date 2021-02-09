from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date',
        'comment',
    )

    ordering = ('date',)


admin.site.register(Review, ReviewAdmin)
