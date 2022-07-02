from django.shortcuts import render

def checkout(request):
    """ View for checkout page """


    return render(request, 'checkout/checkout.html')