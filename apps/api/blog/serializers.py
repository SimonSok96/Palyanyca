from rest_framework import serializers

from apps.blog.models import Article
from apps.catalog.models import Category, Product, Image


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = (
            'id',
            'category',
            'user',
            'image',
            'title',
            'text_preview',
            'text',
        )
