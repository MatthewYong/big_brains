from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from toys.models import Toy
from .forms import ToyReviewForm


def toy_detail(request, toy_id):
    """
    A view to show single toy and its user reviews.
    In toy_reviews we get all the objects from the
    ToyReview model and through the filter method we can
    filter all the reviews by a specific toy's id.
    """

    toy = get_object_or_404(Toy, pk=toy_id)
    toy_reviews = ToyReview.objects.all().filter(toy=toy)
    toy_review_form = ToyReviewForm()

    context = {
        'toy': toy,
        'toy_reviews': toy_reviews,
        'toy_review_form': toy_review_form,
    }
    return render(request, 'toys/toy_detail.html', context)


def add_toy_review(request, toy_id):
    """
    A view to add a review for a specific toy
    """

    if request.method == 'POST':
        toy = get_object_or_404(Toy, pk=toy_id)
        redirect_url = request.POST.get('redirect_url')
        toy_review_form = ToyReviewForm(request.POST)

        if toy_review_form.is_valid():
            instance = toy_review_form.save(commit=False)
            # Sets the foreign key toy to object Toy with pk=toy_id
            instance.toy = toy
            instance.save()
            return redirect(redirect_url)
        else:
            messages.error(request, 'There is something wrong with your form. \
                Please double check your information.')

