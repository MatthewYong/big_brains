from django.shortcuts import render, redirect


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
                    print('Sorry the maximum quantity you can buy is 10')
                    # Add toast message
                else:
                    cart[toy_id] += quantity
            else:
                cart[toy_id] = quantity
        else:
            print('Sorry the maximum quantity you can buy is 10')
            # Add toast message
    request.session['cart'] = cart

    return redirect(redirect_url)


def update_cart(request, toy_id):
    """Function to update the quantity in the user's cart"""
    cart = request.session.get('cart', {})
    update_quantity = int(request.POST.get('update_quantity'))
    redirect_url = request.POST.get('redirect_url')

    if update_quantity < 0 or update_quantity > 10:
        print('Sorry the quantity must be between 0 or 10')
        # Add toast message
    elif update_quantity > 0 and update_quantity <= 10:
        cart[toy_id] = update_quantity
    else:
        cart.pop(toy_id)
        print('Item removed from cart')
        # Add toast message

    request.session['cart'] = cart
    print(cart)

    return redirect(redirect_url)


def remove_from_cart(request, toy_id):
    """Function to remove an item from rhe user's cart"""
    cart = request.session.get('cart', {})
    cart.pop(toy_id)
    print('Item removed from cart')
    # Add toast message

    redirect_url = request.POST.get('redirect_url')

    request.session['cart'] = cart

    return redirect(redirect_url)
