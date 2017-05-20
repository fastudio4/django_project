from django.shortcuts import render
from mysite.models import CategoryManufactures, CategoryCatalog # for base
from mysite.models import CategoryArticle, Article # article content
from mysite.models import Products # catalog products

def template(request):
    cat_pro = CategoryCatalog.objects.order_by('title_cat')
    home_page = Article.objects.all()
    return render(request, 'mysite/template.html', {
        'cat_pro': cat_pro,
        'home_page': home_page
    })

