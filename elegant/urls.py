from django.conf.urls import url, include
from elegant import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.client_list, name='client_list'),
    url(r'^procedure/$', views.procedure, name='procedure'),
    url(r'^shugaring/$', views.shugaring, name='shugaring'),
    url(r'^price/$', views.price, name='price'),
    url(r'^news/$', views.news, name='news'),
    url(r'^contact/$', views.contact, name='contact'),
    url('', include('social.apps.django_app.urls', namespace='social')),


]
