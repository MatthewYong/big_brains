from django.shortcuts import render, redirect


def view_cart(request):
    """A view that shows the cart page"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, toy_id):
    """Add a quantity of toys to the cart"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if toy_id in list(cart.keys()):
        cart[toy_id] += quantity
    else:
        cart[toy_id] = quantity

    request.session['cart'] = cart

    return redirect(redirect_url)
