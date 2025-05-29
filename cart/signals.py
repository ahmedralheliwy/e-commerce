from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import CartItem
from products.models import Product

@receiver(user_logged_in)
def merge_session_cart(sender, request, user, **kwargs):
    session_cart = request.session.get('cart', {})
    
    for product_id, quantity in session_cart.items():
        try:
            product = Product.objects.get(id=product_id)
            cart_item, created = CartItem.objects.get_or_create(user=user, product=product)
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
                cart_item.save()
        except Product.DoesNotExist:
            continue
    # Clear the session cart after merging
    if 'cart' in request.session:
        del request.session['cart']
        request.session.modified = True