from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product

# Pagination
from django.core.paginator import Paginator


def all_products(request):
    """ Show all products including sort by and search queries """

    # Set up pagination
    p = Paginator(Product.objects.all(), 10)
    page = request.GET.get('page')
    products = p.get_page(page)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You dodn't enter any search criteria")

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def prodsuct_detail(request, product_id):
    """ how individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
