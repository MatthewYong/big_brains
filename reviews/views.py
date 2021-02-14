from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from toys.models import Toy
from .forms import ToyReviewForm


@login_required
def add_toy_review(request, toy_id):
    """
    A view to add a review for a specific toy.
    The view gets the ID from a specific toy and
    links it to the filled form
    """

    if request.method == 'POST':
        toy = get_object_or_404(Toy, pk=toy_id)
        redirect_url = request.POST.get('redirect_url')
        toy_review_form = ToyReviewForm(request.POST)

        if toy_review_form.is_valid():
            instance = toy_review_form.save(commit=False)
            # Sets the foreign key toy to object Toy with pk=toy_id
            instance.toy = toy
            # Sets the foreign key user to object user_review with user_id
            instance.user_review = request.user
            instance.save()
            return redirect(redirect_url)
        else:
            messages.error(request, 'There is something wrong with your form. \
                Please double check your information.')
