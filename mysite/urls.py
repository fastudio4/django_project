from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.template, name='template'),
    # url(r'^(?P<title_pro>\w+)/$', views.product, name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
