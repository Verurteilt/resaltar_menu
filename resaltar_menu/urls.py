from django.conf.urls import patterns, include, url
from menu.views import inicio, nosotros


urlpatterns = patterns('',
    url(r'^$', inicio, name='home'),
    url(r'^nosotros/', nosotros, name='about'),
)
