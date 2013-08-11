from django.conf.urls import patterns, include, url
from nauka_django.views import hello, strona glowna

urlpatterns = patterns('',
                       url(r'^hello/$', hello),
                       url(r'^$', strona_glowna),
   
)
