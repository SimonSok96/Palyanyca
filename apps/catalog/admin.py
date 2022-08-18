from django.contrib import admin
from apps.catalog.models import Category, Product, Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


class ProductCategoryInline(admin.TabularInline):
    model = Product.categories.through
    extra = 1

class ImageInline(admin.TabularInline):
    model = Image
    fields = ['product', 'image_teg', 'image', 'is_main']
    readonly_fields = ['image_teg']
    extra = 1



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'quantity', 'price']
    # list_display_links = ['id', 'mane']
    # fields = ['name', 'description', 'quantity', 'price']
    inlines = [ProductCategoryInline, ImageInline]

