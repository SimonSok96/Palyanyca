from django.contrib import admin
from apps.blog.models import Article, BlogCategory, Teg


admin.site.register(Article)
admin.site.register(BlogCategory)
admin.site.register(Teg)