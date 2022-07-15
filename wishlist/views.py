from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from profiles.models import UserProfile
from products.models import Product
from wishlist.models import Wishlist


@login_required
def wishlist(request):
    """ Display a specific user's wishlst """
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
    Add a wishlist item from the current product on product_detail
    """
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    my_wishlist = Wishlist.objects.filter(user_profile=user, product=product)
    if my_wishlist.count() >= 1:
        messages.info(request, f"{product.name} is already on your Wishlist!")
    else:
        Wishlist.objects.create(product=product, user_profile=user)
        messages.info(request, f"You've added {product.name} to your Wishlist!")

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def delete_wishlist_item(request, product_id):
    """
    Delete a wishlist item from a button/icon in the wishlist.html template
    """
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    Wishlist.objects.filter(product=product, user_profile=user).delete()

    messages.info(request, f"You've removed {product.name} \
                            from your Wishlist!")
    template = 'wishlist/wishlist.html'

    my_wishlist = Wishlist.objects.filter(user_profile=user)

    context = {
            'my_wishlist': my_wishlist,
            }
    return render(request, template, context)
