from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from .models import Toy, Age


def all_toys(request):
    """A view that shows all the toys page,\
    which includes searching and sorting features """

    toys = Toy.objects.all()
    query = None
    age = None
    # Code used from Boutique Ado - CI Lesson
    if request.GET:
        if 'age' in request.GET:
            ages = request.GET['age'].split(',')
            toys = toys.filter(age__name__in=ages)
            ages = Age.objects.filter(name__in=ages)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search request")
                return redirect(reverse('toys'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            toys = toys.filter(queries)

    context = {
        'toys': toys,
        'search_toys': query,
        'age_range': age,
    }

    return render(request, 'toys/toys.html', context)


def toy_detail(request, toy_id):
    """A view that shows a single toy page"""

    toy = get_object_or_404(Toy, pk=toy_id)

    context = {
        'toy': toy,
    }

    return render(request, 'toys/toy_detail.html', context)


def all_reviews(request):
    """
    A view to get all the reviews for each specific toy
    """


    context = {
        'reviews': reviews,
    }

    return render(request, 'toys/toys.html', context)
