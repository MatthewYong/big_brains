from django.shortcuts import render, redirect


def view_cart(request):
    """A view that shows the cart page"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, toy_id):
    """Add a quantity of toys to the cart"""
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


def remove_from_cart(request, toy_id):
    cart = request.session.get('cart', {})
    cart.pop(toy_id)

    request.session['cart'] = cart
    print(cart)
    return redirect('toys')