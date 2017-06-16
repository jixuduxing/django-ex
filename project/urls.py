from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health,log
from weixin.views import hello,Weixin
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^weixin$', csrf_exempt(Weixin.as_view())),
    url(r'^health$', health),
    url(r'^log$', log),
    url(r'^admin/', include(admin.site.urls)),
]
