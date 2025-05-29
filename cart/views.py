from django.shortcuts import render, redirect
from cart.models import CartItem
from products.models import Product
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        return render(request, 'cart/cart_empty.html')
    else:
        total_price = sum(item.get_total_price() for item in cart_items)

        context = {
        'cart_items': cart_items,
        'total_price': total_price,
         }
        return render(request, 'cart/cart.html', context)

def add_cart_view(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        product = Product.objects.get(id=product_id)
        
        if request.user.is_anonymous:
            cart=request.session.get('cart', {})
            str_id = str(product.id)
            if str_id in cart:
                cart[str_id] += quantity
            else:
                cart[str_id] = quantity
            request.session['cart'] = cart
        else:
            cart_item, created = CartItem.objects.get_or_create(
                user=request.user,
                product=product,
                defaults={'quantity': quantity}
            )

            if not created:
                cart_item.quantity += quantity
                cart_item.save()

        return redirect('cart:cart')
@login_required
def update_cart_view(request):
    if request.method == 'POST':
        cart_item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity', 1))
        cart_item = get_object_or_404(CartItem, id=cart_item_id)

        if cart_item.user == request.user:
            cart_item.quantity = quantity
            cart_item.save()

        return redirect('cart:cart')
    else:
        return redirect('core:home')  # redirect to home page if not a post request