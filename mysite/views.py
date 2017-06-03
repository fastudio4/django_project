from django.core.exceptions import ObjectDoesNotExist
from django.http import response, Http404
from django.shortcuts import render, get_object_or_404, redirect
from mysite.models import CategoryCatalog, Article, Products, Comments
from mysite.forms import TestForm, CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout


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
    last_article = Article.objects.filter(category_article=2).order_by('create_article')[:5]
    blog_page = Article.objects.filter(category_article=2).order_by('create_article')
    paginator_page = Paginator(blog_page, 3)
    page = request.GET.get('page')

    try:
        content_page = paginator_page.page(page)
    except PageNotAnInteger:
        content_page = paginator_page.page(1)
    except EmptyPage:
        content_page = paginator_page.page(paginator_page.num_pages)
    context = {

        'blog_page': content_page,
        'paginator_count': paginator_page.page_range,
        'articles': last_article,
    }
    return render(request, 'mysite/blog.html', context)

def article(request, pk):
    article_one = get_object_or_404(Article, pk=pk)
    comment = Comments.objects.filter(comment_article=pk).order_by('pk')
    form = CommentForm
    articles = Article.objects.filter(category_article=2).order_by('create_article')[:5]
    context = {
        'article_one': article_one,
        'articles': articles,
        'comments': comment,
        'comment_form': form,
        'user': auth.get_user(request).username
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

def addlike(request, pk):
    try:
        if pk in request.COOKIES:
            redirect('/blog/%s' % pk)
        else:
            add = Article.objects.get(pk=pk)
            add.like += 1
            add.save()
            response = redirect('/blog/%s' % pk)
            response.set_cookie(pk, 'test')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/blog/%s' % pk)

def comments(request, pk):
    if request.POST and ('block' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_article = Article.objects.get(pk=pk)
            form.save()
            request.session.set_expiry(60)
            request.session['block'] = True
    return redirect('/blog/%s' % pk)


def login(request):
    if request.POST:
        username = request.POST.get['user']
        password = request.POST.get['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            return redirect('/')
        else:
            context = {'error_login': 'Incorrect username or password'}
            return render(request, 'mysite/login.html', context)
    else:
        return redirect('/')

def logout_(request):
    logout(request)
    return redirect('/')