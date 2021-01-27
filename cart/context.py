from django.shortcuts import get_object_or_404
from toys.models import Toy


def cart_contents(request):
    """Returns the cart items throughout the website through context"""
    cart_items = []
    total = 0
    subtotal = 0
    toy_count = 0
    cart = request.session.get('cart', {})

    for toy_id, quantity in cart.items():
        toy = get_object_or_404(Toy, pk=toy_id)
        total += quantity * toy.price
        subtotal += quantity * toy.price
        toy_count += quantity
        cart_items.append({
            'toy_id': toy_id,
            'quantity': quantity,
            'toy': toy,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'subtotal': subtotal,
        'toy_count': toy_count,
    }

    return context
