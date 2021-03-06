from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Avg
from django.db.models.functions import Lower

from .models import Product, Category
from profiles.models import UserProfile
from reviews.models import ProductReview
from reviews.forms import ReviewForm
from .forms import ProductForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def all_products(request):
    """ Show all products including sort by and search queries """
    query = None
    categories = None
    sort = None
    direction = None

    products_list = Product.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(products_list, 8)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products_list.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                products = products_list.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

                products = products_list.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products_list.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def lighter_yarn_weights(request):
    """ View to return lighter yarns from homepage link """
    products = Product.objects.filter(weight__icontains='Light')

    template = 'products/products.html'

    context = {
            'products': products,
        }

    return render(request, template, context)


def product_detail(request, product_id):
    """
    Show individual product details
    Display reviews associated with product
    Don't provide a review form is user not authenticated
    """

    product = get_object_or_404(Product, pk=product_id)
    reviews = ProductReview.objects.all().filter(product=product)
    mean_rating = reviews.aggregate(Avg('rating'))['rating__avg']

    if mean_rating is not None:
        mode_rating = round(mean_rating)
    else:
        mode_rating = 0

    if not request.user.is_authenticated:
        template = 'products/product_detail.html'
        context = {
            'product': product,
            'reviews': reviews,
            'mode_rating': mode_rating,
        }
        return render(request, template, context)

    review_form = ReviewForm()
    new_review = None

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid:
            new_review = review_form.save(commit=True)
            new_review.product = product
            new_review.save()
        else:
            review_form = ReviewForm()

    template = 'products/product_detail.html'

    context = {
        'product': product,
        'reviews': reviews,
        'review_form': review_form,
        'new_review': new_review,
        'mode_rating': mode_rating,
    }

    return render(request, template, context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. \
                         Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. \
                    Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def post_review(request, product_id):
    """
    Create a product review
    Post to product detail template
    User must be authenticated to leave a review
    Give feedback to user if posted or not
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = product
            review.user_profile = get_object_or_404(
                UserProfile, user=request.user)
            review.save()
            messages.success(
                request, 'Your review has been posted!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add review. Please ensure the form \
                    is valid')
    context = {
        'review_form': review_form,
    }

    return render(request, context)
