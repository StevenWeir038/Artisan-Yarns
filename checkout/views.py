from django.shortcuts import render


def checkout(request):
    """ Checkout page view """

    return render(request, 'checkout/checkout.html')
