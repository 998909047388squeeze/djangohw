from django.contrib import admin

from .models import CategoryModel, ProductModel, NewsCategoryModel, NewsModel, CartModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['category_name']
    list_display = ['id', 'category_name', 'created_at']
    list_filter = ['created_at']
    ordering = ['id']


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    search_fields = ['products_name']
    list_display = ['id', 'products_name', 'price', 'count', 'created_at']
    list_filter = ['created_at']
    ordering = ['-id']

@admin.register(NewsCategoryModel)
class NewsCategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['category_name']
    list_display = ['id', 'category_name', 'created_at']
    list_filter = ['created_at']
    ordering = ['-id']

@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    search_fields = ['title_name']
    list_display = ['id', 'title_name', 'category', 'created_at']
    list_filter = ['created_at']
    ordering = ['-id']

@admin.register(CartModel)
class CartModelAdmin(admin.ModelAdmin):
    search_fields = ['user_id, user_product']
    list_display = ['user_id', 'user_product', 'user_product_quantity', 'user_add_date']
    list_filter = ['user_add_date']
    ordering = ['-user_id']