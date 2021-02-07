from django.shortcuts import render, get_object_or_404

from .models import Blog
from .forms import BlogForm


def all_blogs(request):
    """A view to show the fields of each blog"""

    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blogs/blogs.html', context)


def blog_detail(request, blog_id):
    """
    A view to show the fields of the blog
    """

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blogs/blog_detail.html', context)


def blog_add(request):
    """
    A view to add new blogs through a user profile
    """

    blog_form = BlogForm()
    template = 'blogs/blog_add.html'

    context = {
        'blog_form': blog_form,
    }

    return render(request, template, context)
