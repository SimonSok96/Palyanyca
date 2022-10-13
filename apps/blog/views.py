from django.shortcuts import render
from django.urls import reverse

from apps.blog.forms import CommentForm
from apps.blog.models import BlogCategory, Article, Teg, Comment
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
    comments = Comment.objects.filter(article=article, is_checked=True)
    breadcrumbs = {
        reverse('blog_category_list'): PAGE_NAMES['blog'],
        reverse('article_list', args=[category.id]): category.name,
        'current': article.title
    }
    error = None

    if request.method == 'POST':
        data = request.POST.copy()
        data.update(article=article)
        user = request.user
        if not user.is_anonymous:
            data.update(user=user, name=user.username, email=user.email, is_checked=True)
        request.POST = data
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/article/created.html', {'article': article})
        else:
            error = form.errors

    return render(
        request,
        'blog/article/view.html',
        {'article': article, 'category': category, 'breadcrumbs': breadcrumbs, 'error': error, 'comments': comments}
    )


def teg_search_article_list(request, teg_id):
    teg = Teg.objects.get(id=teg_id)
    articles = Article.objects.filter(tegs__in=[teg_id])
    return render(request, 'blog/article/teg_search.html', {'articles': articles})
