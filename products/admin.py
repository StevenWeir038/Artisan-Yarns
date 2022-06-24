from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'brand', 'description']
    list_display = (
        'name',
        'category',
        'weight',
        'brand',
        'description',
        'price',
        'image',
    )
    list_filter = ('category', 'weight', 'brand')

    ordering = ('brand','name','price',)
