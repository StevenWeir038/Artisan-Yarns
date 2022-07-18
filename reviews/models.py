from django.db import models

from profiles.models import UserProfile
from products.models import Product


class ProductReview(models.Model):
    """ Product reviews """

    RATING = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING)
    review_title = models.TextField(max_length=254)
    review_description = models.TextField(max_length=500)

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return f'User: {self.user_profile} | Product: {self.product} | Rating: {self.rating}'
