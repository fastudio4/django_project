from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/(?P<pk>\w+)/$', views.article, name='article'),
    url(r'^contacts/$', views.contacts, name='contacts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
