from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")

def strona_glowna(request):
    return HttpResponse("To jest strona glowna mojego pierwszego projektu Django")