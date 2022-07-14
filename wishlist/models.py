from django.db import models


class Wishlist(models.Model):
    """ Wishlist model (for authenticated users only) """
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"({self.user_profile}'s) WishList"
