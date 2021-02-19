from django import template


register = template.Library()


@register.filter(name='order_subtotal')
def order_subtotal(price, quantity):
    """
    Function calculate the subtotal of the profile orders page
    """
    return price * quantity
