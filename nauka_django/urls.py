from django.conf.urls import patterns, include, url
from nauka_django.views import hello, strona_glowna, current_datetime

urlpatterns = patterns('',
                       url(r'^hello/$', hello),
                       url(r'^$', strona_glowna),
                       url(r'^time/$', current_datetime),
   
)
