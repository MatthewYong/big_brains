from django import template


register = template.Library()


@register.filter(name='cart_subtotal')
def cart_subtotal(price, quantity):
    return price * quantity
