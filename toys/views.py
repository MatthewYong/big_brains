from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from .models import Toy, Age, ToyReview
from .forms import ToyReviewForm


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
    """A view to show single toy and its user reviews"""

    toy_review_form = ToyReviewForm()
    toy = get_object_or_404(Toy, pk=toy_id)
    toy_reviews = ToyReview.objects.all().filter(toy=toy)

    context = {
        'toy_review_form': toy_review_form,
        'toy': toy,
        'toy_reviews': toy_reviews,
    }
    return render(request, 'toys/toy_detail.html', context)


def add_toy_review(request, toy_id):
    """
    A view to add a review for a specific toy
    """

    if request.method == 'POST':

        redirect_url = request.POST.get('redirect_url')
        toy_review_form_data = {
            'name': request.POST['name'],
            'comment': request.POST['comment'],
        }

        toy_review_form = ToyReviewForm(toy_review_form_data)

        if toy_review_form.is_valid():
            instance = toy_review_form.save(commit=False)
            instance.toy = request.GET.get(toy_id)
            instance.save()
            return redirect(redirect_url)
        else:
            messages.error(request, 'There is something wrong with your form. \
                Please double check your information.')
