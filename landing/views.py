from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from toys.models import Toy


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

    context = {
        'toys': toys,
    }

    return render(request, 'landing/index.html', context)


def tempview(request):
    """
    Temporary view to render temp.html
    """

    return render(request, 'landing/temp.html')
