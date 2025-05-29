from django.urls import path
from .views import cart_view, add_cart_view, update_cart_view

app_name = 'cart'

urlpatterns = [
    path('', cart_view, name='cart'),
    path('add/<int:product_id>/', add_cart_view, name='add_cart'),
    path('update/', update_cart_view, name='update_cart'),
]

    # Add more cart-related URLs as needed
    # path('remove/', remove_cart_view, name='remove_cart'),