from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings

from toys.models import Toy
from blogs.models import Blog


def index(request):
    """
    A view that shows the landing page and sends
    an email to the user
    """

    if request.method == 'POST':
        message = request.POST['message']
        send_mail('Contact Form Big Brains',
                  message,
                  settings.EMAIL_HOST_USER,
                  ['kfm.yong@gmail.com'],
                  fail_silently=False)

    toys = Toy.objects.all()
    blogs = Blog.objects.all()

    context = {
        'toys': toys,
        'blogs': blogs,
    }

    return render(request, 'landing/index.html', context)


def view_toy_detail(request, toy_id):
    """
    A view to redirect the user to the toy's detailed page
    """

    toy = get_object_or_404(Toy, pk=toy_id)

    context = {
        'toy': toy,
    }

    return render(request, 'toys/toy_detail.html', context)


def tempview(request):
    """
    Temporary view to render temp.html
    """

    return render(request, 'landing/temp.html')
