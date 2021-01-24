

def cart_contents(request):

    cart_items = []
    total = 0
    toys_count = 0

    context = {
        'cart_items': cart_items,
        'total': total,
        'toys_count': toys_count,
    }

    return context
