from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'original_price', 'rating', 'sales_count', 'stock', 'category', 'location', 'is_featured')
    list_filter = ('category', 'is_featured', 'location')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
