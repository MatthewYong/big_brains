from django.shortcuts import render, redirect
from django.contrib import messages


def view_cart(request):
    """A view that shows the cart page"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, toy_id):
    """Function to add a quantity in the user's cart"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if quantity <= 0:
        print('Sorry the minimum quantity you have to buy is 1')
        # Add toast message
    else:
        if quantity > 0 and quantity <= 10:
            if toy_id in list(cart.keys()):
                # Prevents user from adding more toy qty than 10
                if quantity + cart[toy_id] > 10:
                    messages.warning(
                        request,
                        'Sorry, the maximum quantity you can buy is 10')
                else:
                    cart[toy_id] += quantity
                    messages.success(request, 'Added to Cart')
            else:
                cart[toy_id] = quantity
                messages.success(request, 'Added to Cart')
        else:
            messages.warning(
                request, 'Sorry, the maximum quantity you can buy is 10')
    request.session['cart'] = cart

    return redirect(redirect_url)


def update_cart(request, toy_id):
    """Function to update the quantity in the user's cart"""
    cart = request.session.get('cart', {})
    update_quantity = int(request.POST.get('update_quantity'))
    redirect_url = request.POST.get('redirect_url')

    if update_quantity < 0 or update_quantity > 10:
        messages.warning(
            request, 'Sorry, the quantity must be between 0 or 10')
    elif update_quantity > 0 and update_quantity <= 10:
        cart[toy_id] = update_quantity
        messages.warning(
            request, 'Cart is up-to-date')
    else:
        cart.pop(toy_id)
        messages.error(request, 'Removed from Cart')
    request.session['cart'] = cart

    return redirect(redirect_url)


def remove_from_cart(request, toy_id):
    """Function to remove an item from the user's cart"""
    cart = request.session.get('cart', {})
    cart.pop(toy_id)
    messages.error(request, 'Removed from Cart')
    redirect_url = request.POST.get('redirect_url')
    request.session['cart'] = cart

    return redirect(redirect_url)
