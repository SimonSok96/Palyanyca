from rest_framework import serializers

from apps.blog.models import Article, Teg
from apps.catalog.models import Category, Product, Image


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teg
        fields = '__all__'


class ArticleReadSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=Teg)

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


class ArticleWriteSerializer(serializers.ModelSerializer):
    tegs = serializers.ListField(child=serializers.CharField(max_length=64))

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
            'tegs',
        )
