from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Profile


@login_required
def profile(request):
    """
    Function to link the order history to a specific user
    """
    profile = get_object_or_404(Profile, user=request.user)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)
