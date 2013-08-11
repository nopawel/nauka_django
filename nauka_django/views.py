from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def strona_glowna(request):
    return HttpResponse("To jest strona glowna mojego pierwszego projektu Django")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>Taka mamy godzine %s.</body></html>" % now
    return HttpResponse(html)