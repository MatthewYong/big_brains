from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'author_friendly',
        'date',
        'title',
        'description',
        'article',
        'image_url',
    )

    ordering = ('author',)


admin.site.register(Blog, BlogAdmin)
