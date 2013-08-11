from django.conf.urls import patterns, include, url
from nauka_django.views import hello

urlpatterns = patterns('',
                       url(r'^hello/$', hello),
   
)
