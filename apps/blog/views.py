from django.shortcuts import render
from apps.blog.models import BlogCategory, Article, Teg
from config.settings import PAGE_NAMES


def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    #breadcrumds = {'current': PAGE_NAMES['blog']}
    return render(request, 'blog/category/list.html', {'categories': blog_categories})


def article_list(request, category_id):
    articles = Article.objects.filter(category=category_id)
    #breadcrumds = {reverse('blog_category_list'): PAGE_NAMES['blog'], 'current': category.name}
    return render(request, 'blog/article/list.html', {'articles': articles})


def article_view(request, category_id, article_id):
    article = Article.objects.get(id=article_id)
    category = BlogCategory.objects.get(id=category_id)
    return render(request, 'blog/article/view.html', {'article': article, 'category': category})


def teg_search_article_list(request, teg_id):
    teg = Teg.objects.get(id=teg_id)
    articles = Article.objects.filter(tegs__in=[teg_id])
    return render(request, 'blog/article/teg_search.html', {'articles': articles})
