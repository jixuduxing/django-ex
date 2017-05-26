from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health
from weixin.views import hello


urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^weixin$', hello),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
]
