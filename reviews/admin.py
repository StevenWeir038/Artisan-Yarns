from django.contrib import admin
from .models import ProductReview


admin.site.register(ProductReview)


class ProductReviewAdmin(admin.ModelAdmin):
    """
    Display list of Reviews
    Allow admin to filter by ratings
    Order by most recent reviews and ratings
    """

    model = ProductReview

    search_fields = ['product', 'rating', 'user_profile']

    list_display = (
        'added_on',
        'product',
        'rating',
        'review_description',
        'user_profile',
    )

    list_filter = ('product', 'rating', 'user_profile',)

    ordering = ('-added_on', '-rating', )
