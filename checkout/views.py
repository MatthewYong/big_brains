from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from toys.models import Toy
from cart.context import cart_contents

import stripe


def checkout(request):
    """
    A view to get the items from the cart
    and pass it into the checkout form.
    Code used from CI checkout and Stripe lessons
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email_address': request.POST['email_address'],
            'address': request.POST['address'],
            'postcode': request.POST['postcode'],
            'town': request.POST['town'],
            'country': request.POST['country'],
            'comments': request.POST['comments'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                toy = Toy.objects.get(id=item_id)
                order_line_item = OrderLineItem(
                    order=order,
                    toy=toy,
                    quantity=item_data,
                )
                order_line_item.save()
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
            print(order_form.errors)
            return redirect(reverse('checkout_success'))

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, 'Your cart is empty')
            return redirect(reverse('toys'))

        current_cart = cart_contents(request)
        total = current_cart['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Please fill in the correct Stripe \
            Public key')

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


def checkout_success(request, order_number):
    """
    After checkout is successful, cart will be emptied
    and success message will be displayed
    """
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        # Order will be added to order history of user's profile
        order.profile = profile
        order.save()

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
