from django.shortcuts import render, get_object_or_404

from .models import Profile
from checkout.models import Order


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


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
