from django.urls import path
from .views import order_list, checkout

app_name = 'orders'

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('', order_list, name='order_list'),
]