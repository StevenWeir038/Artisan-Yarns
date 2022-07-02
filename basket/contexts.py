from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += item_data * product.price
        product_count += item_data
        basket_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'product': product,
        })

    context = {
        'basket_items': basket_items,
        'product_count': product_count,
        'total': total,
    }

    return context
