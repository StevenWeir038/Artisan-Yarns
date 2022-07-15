from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from profiles.models import UserProfile
from products.models import Product
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


@login_required
def add_wishlist_item(request, product_id):
    """
    Add a wishlist item from a product
    Think - get the product id from product details and pass to wishlist
    """
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    # Only need to create a wishlist object
    # No need to render anything to a template
    # Redirect back to same page as button
    # This only exists in the product details template at the moment
    Wishlist.objects.create(user_profile=user, product=product)

    return redirect(reverse('product_detail', args=[product.id]))
