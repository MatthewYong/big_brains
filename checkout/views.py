from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """
    A view to get the items from the cart
    and pass it into the checkout form.
    Code used from CI checkout lesson
    """
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Your cart is empty')
        return redirect(reverse('toys'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_3BCW3Acv1kXy7DGzsX4h4tUq00aM1HcTxr',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
