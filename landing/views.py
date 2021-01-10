from django.shortcuts import render


def index(request):
    """A view that shows the index page"""
    return render(request, 'landing/index.html')
