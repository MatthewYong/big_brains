from django.shortcuts import render, redirect


def view_cart(request):
    """A view that shows the cart page"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """Add a quantity of toys to the cart"""
    quantity = int(request.POSt.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
