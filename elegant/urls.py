from django.conf.urls import url
from elegant import views

urlpatterns = [
    url(r'^$', views.client_list, name='client_list'),
    url(r'^procedure/$', views.procedure, name='procedure'),
    url(r'^shugaring/$', views.shugaring, name='shugaring'),
    url(r'^price/$', views.price, name='price'),
    url(r'^news/$', views.news, name='news'),
]
