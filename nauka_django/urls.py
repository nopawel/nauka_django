from django.conf.urls import patterns, include, url
from nauka_django.views import hello, strona_glowna, current_datetime, hours_ahead

urlpatterns = patterns('',
                       url(r'^hello/$', hello),
                       url(r'^$', strona_glowna),
                       url(r'^time/$', current_datetime),
                       url(r'^time/plus/(\d{1,2})/$', hours_ahead),
)
