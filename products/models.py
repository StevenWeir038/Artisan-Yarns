from django.db import models


class Category(models.Model):
    """ Category model """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ Product model """

    class ProductBrand(models.TextChoices):
        """ subclass choices for brands """
        YUMMY = 'Yummy'
        ADRIAFIL = 'Adriafil'
        SCHEEPJES = 'Scheepjes'
        NEWFASHION = 'New Fashion'
        OTHER = 'Other'

    class ProductWeight(models.TextChoices):
        """ subclass choices for weights """
        SUPER_FINE = 'SuperFine (Baby, Fingering, Sock)'
        FINE = 'Fine (Baby, Sport)'
        LIGHT = 'Light (DK, Light, Worsted)'
        MEDUIM = 'Meduim (Afgan, Aran, Worsted)'
        BULKY = 'Bulky (Chunky, Craft, Rug)'
        SUPER_BULKY = 'Super Bulky (Bulky, Roving)'
        JUMBO = 'Jumbo (Jumbo, Roving)'
        OTHER = 'Other'

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    brand = models.CharField(max_length=20, choices=ProductBrand.choices, null=True, blank=True,)
    weight = models.CharField(max_length=50, choices=ProductWeight.choices, null=True, blank=True,)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
