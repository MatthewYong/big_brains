from django.shortcuts import render
from .models import Blog


def all_blogs(request):
    """A view to show the fields in the blog"""

    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blogs/blogs.html', context)

