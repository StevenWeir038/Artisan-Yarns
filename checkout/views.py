from django.shortcuts import render, redirect, reverse
from django.contrib import messages

def checkout(request):
    """ View for checkout page """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "The basket is empty")

    return redirect(reverse('products'))
