from django.shortcuts import render


def wishlist(request):
    """ Wishlist page view """

    return render(request, 'wishlist/wishlist.html')
