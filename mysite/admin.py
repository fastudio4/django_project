from django.contrib import admin

from mysite.models import CategoryCatalog, Products, Manufactures, CategoryManufactures,  NavbarMenu, CategoryArticle, Article


admin.site.register(CategoryCatalog)
admin.site.register(Products)

class CategoryManufacturesAdmin(admin.ModelAdmin):
    list_display = ('name_category_man', 'parent_category_man')
admin.site.register(CategoryManufactures, CategoryManufacturesAdmin)

class ManufacturesAdmin(admin.ModelAdmin):

    list_display = ('title_man',)
admin.site.register(Manufactures, ManufacturesAdmin)

class NavbarMenuAdmin(admin.ModelAdmin):
    list_display = ('name_menu', 'parent_menu', 'type_menu', 'position_menu')
admin.site.register(NavbarMenu, NavbarMenuAdmin)

class CategoryArticleAdmin(admin.ModelAdmin):
    list_display = ('title_cat',)
admin.site.register(CategoryArticle, CategoryArticleAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title_article', 'category_article', 'create_article', 'active_article')
    list_filter = ('create_article','active_article')
    search_fields = ('title_article', 'description_article')
admin.site.register(Article, ArticleAdmin)

