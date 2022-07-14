from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def wishlist(request):
    """ 
    Display a specific user's wishlst 
    Need to to pass a dictionary similar to the basket to template
    """

    template = ''
    context = {}

    return render(request, 'wishlist/wishlist.html', context)
