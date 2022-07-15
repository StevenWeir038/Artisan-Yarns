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

    Wishlist.objects.create(user_profile=user, product=product)

    messages.info(request, f"You've added {product.name} to your Wishlist!")

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def delete_wishlist_item(request, product_id):
    """
    Add a wishlist item from the current product on product_detail
    Same approach as add_wishlist_item - get user, get product_id
    Link this view/function to a button/icon in wishlist.html template
    Similar to Kennel project - find a single entry with a filter and delete
    Feedback the action to the user
    
    """
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)


    messages.info(request, f"You've removed {product.name} from your Wishlist!")
    template = 'wishlist/wishlist.html'

    return render(request, template)
