from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'author',
        'description',
        'story',
        'image',
    )

    ordering = ('author',)


admin.site.register(Blog, BlogAdmin)
