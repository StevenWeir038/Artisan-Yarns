from django.shortcuts import render, get_object_or_404
from .models import Product

# Pagination
from django.core.paginator import Paginator


def all_products(request):
    """ A view to show all products including sort by and search queries """

    # Set up pagination
    p = Paginator(Product.objects.all(), 10)
    page = request.GET.get('page')
    products = p.get_page(page)

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
