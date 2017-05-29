from django.shortcuts import render, get_object_or_404
from mysite.models import CategoryCatalog, Article, Products
from mysite.forms import TestForm


def home(request):
    cat_pro = CategoryCatalog.objects.order_by('pk')
    home_page = Article.objects.filter(category_article=1).order_by('create_article')
    article_blog = Article.objects.filter(category_article=2).order_by('create_article')[:4]
    context = {
        'cat_pro': cat_pro,
        'home_page': home_page,
        'blog': article_blog
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


def products(request, title_cat):
    category = CategoryCatalog.objects.get(title_cat=title_cat)
    products_cat = Products.objects.filter(category_pro=category)

    context = {
        'products': products_cat,
        'category': category.title_cat
    }
    return render(request, 'mysite/products.html', context)

def product(request, title_cat, code_pro):
    product_page = Products.objects.get(code_pro=code_pro)
    category_page = CategoryCatalog.objects.get(title_cat=title_cat)
    context = {
        'product': product_page,
        'category': category_page
    }
    return render(request, 'mysite/page_product.html', context)