from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

# Pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def all_products(request):
    """ Show all products including sort by and search queries """
    query = None
    products = None
    categories = None
    weights = None
    sort = None
    direction = None

    # Set up pagination
    products_list = Product.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(products_list, 10)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'weight_light' in request.GET:
            weights = products_list.filter(weight__icontains='light')

        if 'range' in request.GET:
            range = products_list.filter(brand__icontains='Scheepjes')

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products_list.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Create search by brand and weight here.  Will need to add to dropdown menu.
        # Shortcuts from homepage now redundant as individual options needed for
        # each brand option.

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products_list.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'weights': weights,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
