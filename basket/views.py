from django.shortcuts import render


def view_basket(request):
    """ View the shopping basket """

    return render(request, 'basket/basket.html')
