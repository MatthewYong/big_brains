from django.shortcuts import render, get_object_or_404

from .models import Profile


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
