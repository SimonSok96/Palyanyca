from rest_framework import serializers
from apps.catalog.models import Category, Product, Image


class CategorySerializer(serializers.ModelSerializer):
    meta_title = serializers.CharField(write_only=True)
    meta_description = serializers.CharField(write_only=True)
    meta_keywords = serializers.CharField(write_only=True)
    slug = serializers.CharField(write_only=True)
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'description',
            'parent',
            'image',
            'meta_title',
            'meta_description',
            'meta_keywords',
        )


class ProductWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'quantity',
            'price',
        )


class ProductReadSerializers(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'quantity',
            'price',
            'categories',
        )


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'id',
            'image',
            'product',
            'is_main',
        )
