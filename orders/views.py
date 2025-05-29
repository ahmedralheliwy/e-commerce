from django.shortcuts import render,redirect
from .models import Order, OrderItem
from cart.models import CartItem
from django.contrib.auth.decorators import login_required

@login_required
def checkout(request):
    if request.method == 'POST':
        # Process the order
        cart_items = CartItem.objects.filter(user=request.user)
        total = sum(item.product.price * item.quantity for item in cart_items)
        order = Order.objects.create(user=request.user, total=total)
        
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product.name,
                price=item.product.price,
                quantity=item.quantity
            )
        
        # Clear the cart
        cart_items.delete()
        return redirect('orders:order_list')
        
    
    return render(request, 'orders/checkout.html', {'cart_items': CartItem.objects.filter(user=request.user)})

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})