from django.contrib import admin
from wishlist.models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    """ WishlistAdmin model """
    search_fields = ['user_profile', 'product']

    list_display = (
        'user_profile',
        'product',
    )
    list_filter = ('user_profile', 'product')

    ordering = ('user_profile', 'product',)
