from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(ListView):
    model = Item
    template_name = 'index.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'product-page.html'


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_qs= Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item's quantity was updated!")
            return redirect('ecommerceApp:product', 
            slug=slug
        )
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart!")
            return redirect('ecommerceApp:product', 
            slug=slug
        )
    else:
        ordered_date = timezone.now()
        Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
    return redirect('ecommerceApp:product', 
            slug=slug
        )

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs= Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart!")
            return redirect('ecommerceApp:product', slug=slug)
        else:
            messages.info(request, "This item is not in your cart!")
            return redirect('ecommerceApp:product', slug=slug)    
    else: 
        messages.info(request, "You do not have an active order")
        return redirect("ecommerceApp:product", slug=slug)


def checkout(request):
    return render(request, 'checkout-page.html')
