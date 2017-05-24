from django.shortcuts import render, get_object_or_404
from mysite.models import CategoryCatalog, Article
from mysite.forms import TestForm


def home(request):
    cat_pro = CategoryCatalog.objects.order_by('pk')
    home_page = Article.objects.filter(category_article=1).order_by('create_article')
    context = {
        'cat_pro': cat_pro,
        'home_page': home_page
    }
    return render(request, 'mysite/home.html', context)

def blog(request):
    blog_page = Article.objects.filter(category_article=2).order_by('create_article')
    articles = Article.objects.filter(category_article=2).order_by('create_article')[:5]
    context = {
        'blog_page': blog_page,
        'articles': articles,
    }
    return render(request, 'mysite/blog.html', context)

def article(request, pk):
    article_one = get_object_or_404(Article, pk=pk)
    articles = Article.objects.filter(category_article=2).order_by('create_article')[:5]
    context = {
        'article_one': article_one,
        'articles': articles,
    }
    return render(request, 'mysite/article.html', context)

def contacts(request):
    contact_page = Article.objects.filter(category_article=3)
    form = TestForm()

    context = {
        'contact_page': contact_page,
        'form': form
    }

    if request.method == 'POST':
        name_form = request.POST.get('name')
        email_form = request.POST.get('email')
        context.update({'name_form': name_form, 'email_form': email_form})

    return render(request, 'mysite/contacts.html', context)

def base_category_catalog(request):
    categories = CategoryCatalog.objects.order_by('pk')
    return render(request, 'mysite/catalog.html', {'categories': categories})


#