from django.urls import path
from . import views


urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('add_wishlist_item/<int:product_id>/',
         views.add_wishlist_item, name='add_wishlist_item'),
]
