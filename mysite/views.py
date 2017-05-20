from django.shortcuts import render, get_object_or_404
from mysite.models import CategoryCatalog, Article

def home(request):
    cat_pro = CategoryCatalog.objects.order_by('pk')
    home_page = Article.objects.filter(category_article=1).order_by('create_article')
    return render(request, 'mysite/home.html', {
        'cat_pro': cat_pro,
        'home_page': home_page
    })

def blog(request):
    blog_page = Article.objects.filter(category_article=2).order_by('create_article')
    articles = Article.objects.filter(category_article=2).order_by('create_article')[:5]
    cat_pro = CategoryCatalog.objects.order_by('pk')
    return render(request, 'mysite/blog.html', {
        'blog_page': blog_page,
        'articles': articles,
        'cat_pro': cat_pro
    })

def article(request, pk):
    article_one = get_object_or_404(Article, pk=pk)
    articles = Article.objects.filter(category_article=2).order_by('create_article')[:5]
    cat_pro = CategoryCatalog.objects.order_by('pk')
    return render(request, 'mysite/article.html', {
        'article_one': article_one,
        'articles': articles,
        'cat_pro': cat_pro
    })

def contacts(request):
    contact_page = Article.objects.filter(category_article=3)
    cat_pro = CategoryCatalog.objects.order_by('pk')
    return render(request, 'mysite/contacts.html', {
        'contact_page': contact_page,
        'cat_pro': cat_pro
    })

def base_category_catalog(request):
    cat_pro = CategoryCatalog.objects.order_by('pk')
    return render(request, 'mysite/catalog.html', {'cat_pro': cat_pro})
