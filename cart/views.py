from django.shortcuts import render


def cart(request):
    """A view that shows the cart page"""
    return render(request, 'cart/cart.html')
