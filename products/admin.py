from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'brand',
        'weight',
        'description',
        'price',
        'image',
    )

    ordering = ('category','brand','name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
