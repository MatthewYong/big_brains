from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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


@login_required
def blog_add(request):
    """
    A view to add new blogs through a user profile
    """
    if request.method == 'POST':
        blog_form_data = {
            'image_url': request.POST['image_url'],
            'title': request.POST['title'],
            'author': request.POST['author'],
            'date': request.POST['date'],
            'description': request.POST['description'],
            'article': request.POST['article'],
        }
        blog_form = BlogForm(blog_form_data)
        if blog_form.is_valid():
            blog_form.save()
            return redirect(reverse('blogs'))
        else:
            messages.error(request, 'There is something wrong with your form. \
                Please double check your information.')
    else:
        blog_form = BlogForm()
        template = 'blogs/blog_add.html'

        context = {
            'blog_form': blog_form,
        }
        return render(request, template, context)
