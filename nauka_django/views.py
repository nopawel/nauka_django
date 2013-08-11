from django.http import HttpResponse, Http404
import datetime

def hello(request):
    return HttpResponse("Hello world")

def strona_glowna(request):
    return HttpResponse("To jest strona glowna mojego pierwszego projektu Django")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>Taka mamy godzine %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)