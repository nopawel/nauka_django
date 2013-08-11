from django.conf.urls import patterns, include, url
from nauka_django.views import hello, strona_glowna

urlpatterns = patterns('',
                       url(r'^hello/$', hello),
                       url(r'^$', strona_glowna),
   
)
