from django.conf.urls import url, include
from django.contrib.auth.views import logout
from django.conf import settings
from django.conf.urls.static import static

from elegant import views
from elegant import ui

from django.contrib import admin

from elegant.ui.buch.credit import main as credit
from elegant.ui.buch.debet import main as debet

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

    url(r'^contact/$', views.contact, name='contact'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),

    url(r'^debt/$', credit.in_procedure, name='debt'),
    url(r'^credit/$', credit.in_procedure, name='credit'),
    url(r'^debet/$', debet.in_procedure, name='debet'),

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
