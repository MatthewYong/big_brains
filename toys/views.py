from django.shortcuts import render
from .models import Toy


def all_toys(request):
    """A view that shows all the toys page, which includes searching and sorting features """

    toys = Toy.objects.all()

    context = {
        'toys': toys,
    }

    return render(request, 'toys/toys.html')
