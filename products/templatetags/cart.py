from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(i, cart):
    keys = cart.keys()
    for id in keys:
        id = int(id)
        if id == i.id:
            return True
    return False


# @register.filter(name='subtotal')
# def subtotal(i, cart):
#     values = cart.values()
#     price = i.discounted_price
#     price = int(price)
#     # subtotal = values*price
#     print(values, '----------->', price)
#     return True



