from django.shortcuts import render, get_object_or_404
from .models import Toy


def all_toys(request):
    """A view that shows all the toys page, which includes searching and sorting features """

    toys = Toy.objects.all()

    context = {
        'toys': toys,
    }

    return render(request, 'toys/toys.html', context)


def toy_detail(request, toy_id):
    """A view that shows a single toy page"""

    toy = get_object_or_404(Toy, pk=toy_id)

    context = {
        'toy': toy,
    }

    return render(request, 'toys/toy_detail.html', context)
