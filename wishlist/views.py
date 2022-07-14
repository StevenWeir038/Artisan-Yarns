from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from profiles.models import UserProfile
from wishlist.models import Wishlist


@login_required
def wishlist(request):
    """
    Display a specific user's wishlst
    Need to to pass a dictionary similar to the basket to template
    """
    user = get_object_or_404(UserProfile, user=request.user)
    my_wishlist = Wishlist.objects.filter(user_profile=user)

    template = 'wishlist/wishlist.html'
    context = {
        'my_wishlist': my_wishlist,
        }

    return render(request, template, context)
