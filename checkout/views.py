from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    """ View for checkout page """
    # basket = request.session.get('basket', {})
    # if not basket:
    #     messages.error(request, "The basket is empty")

    # return redirect(reverse('products'))

    # order_form = OrderForm()
    # template = 'checkout/checkout.html'
    # context = {
    #     'order_form': order_form,
    # }

    # return render(request, template, context)

    return render(request, 'checkout/checkout.html')
