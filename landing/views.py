from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    """
    A view that shows the landing page and sends
    an email to the user.
    """

    if request.method == 'POST':
        message = request.POST['message']
        send_mail('Contact Form',
                  message,
                  settings.EMAIL_HOST_USER,
                  ['kfm.yong@gmail.com'],
                  fail_silently=False)

    return render(request, 'landing/index.html')
