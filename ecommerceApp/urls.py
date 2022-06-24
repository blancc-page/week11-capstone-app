from django.urls import path, include
from .views import *

app_name = 'ecommerceApp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name = 'checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name = 'product'),
    path('add_to_cart/<slug>', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>', remove_from_cart, name='remove_from_cart')
]