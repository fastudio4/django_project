from django.shortcuts import render
from mysite.models import NavbarMenu, CategoryManufactures, CategoryCatalog # for base
from mysite.models import CategoryArticle, Article # article content
from mysite.models import Products # catalog products

def template(request):
    menu = NavbarMenu.objects.order_by('position_menu')
    cat_man = CategoryManufactures.objects.all()
    cat_pro = CategoryCatalog.objects.all()
    return render(request, 'mysite/template.html', {
        'menu': menu,
        'cat_man': cat_man,
        'cat_pro': cat_pro

    })


