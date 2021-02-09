from django.shortcuts import render
from .models import Review


def all_reviews(request, toy_id):
    """
    A view to get all the reviews for each specific toy
    """

    reviews = Review.objects.all()
    template = 'toy_detail.html'

    context = {
        'reviews': reviews,
    }

    return render(request, template, context)
