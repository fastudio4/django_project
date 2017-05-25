from django.contrib import admin

from mysite.models import CategoryCatalog, Products, Manufactures, CategoryManufactures, CategoryArticle, Article

admin.site.register(CategoryCatalog)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title_pro', 'category_pro', 'manufactures_pro')
    list_filter = ('manufactures_pro',)
    search_fields = ('title_pro', 'description_article', 'code_pro')

admin.site.register(Products, ProductsAdmin)

class CategoryManufacturesAdmin(admin.ModelAdmin):
    list_display = ('name_category_man', 'parent_category_man')
admin.site.register(CategoryManufactures, CategoryManufacturesAdmin)

class ManufacturesAdmin(admin.ModelAdmin):
    list_display = ('title_man',)
admin.site.register(Manufactures, ManufacturesAdmin)

class CategoryArticleAdmin(admin.ModelAdmin):
    list_display = ('title_cat', 'parent_cat')
admin.site.register(CategoryArticle, CategoryArticleAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title_article', 'category_article', 'create_article', 'active_article')
    list_filter = ('create_article', 'active_article')
    search_fields = ('title_article', 'description_article')
admin.site.register(Article, ArticleAdmin)

