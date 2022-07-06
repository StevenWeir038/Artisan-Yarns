from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """ View for checkout page """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51L3xB3E1oNV7hjVnO5PIJiOhRd0s9gnna3eRGTH7AebvcHBaji5pE93HY9XHa3pcL8bDq9uFENunIXWKNpUGkc9d00ZENrzXnL',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
