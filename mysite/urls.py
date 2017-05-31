from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^catalog/$', views.base_category_catalog, name='base_category'),
    url(r'^catalog/(?P<title_cat>\w+)/$', views.products, name='products'),
    url(r'^catalog/(?P<title_cat>\w+)/(?P<code_pro>[\w-]+)/$', views.product, name='product'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/(?P<pk>[0-9]+)/$', views.article, name='article'),
    url(r'^blog/addlike/(?P<pk>[0-9]+)/$', views.addlike, name='addlike'),
    url(r'^contacts/$', views.contacts, name='contacts'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
