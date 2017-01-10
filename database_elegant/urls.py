from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('elegant.urls')),
    # Social auth
    url('', include('social.apps.django_app.urls', namespace='social')),
]
