from django.conf.urls import url, include
from django.contrib.auth.views import logout
from django.conf import settings
from django.conf.urls.static import static

from elegant import views
from elegant import ui

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.client_list, name='client_list'),
    url(r'^procedure/$', views.procedure, name='procedure'),
    url(r'^shugaring/$', views.shugaring, name='shugaring'),
    url(r'^price/$', views.price, name='price'),

    url(r'^news/$', views.news, name='news'),
    url(r'^news/sale/$', views.news_sale, name='news_sale'),
    url(r'^news/stock/$', views.news_stock, name='news_stock'),
    url(r'^news/novelty/$', views.news_novelty, name='news_novelty'),
    url(r'^news/care/$', views.news_care, name='news_care'),

    url(r'^news/(?P<pk>\d+)/$', views.news_detail, name='news_detail'),

    url(r'^comments/$', views.comments, name='comments'),
    url(r'^contact/$', views.contact, name='contact'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
