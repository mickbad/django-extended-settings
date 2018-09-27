from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

def index(request):
    var = settings.APPLICATION_SENTENCE
    return HttpResponse("<html><body><h2>Welcome here!</h2><p>Configuration is '{}'</p></body></html>".format(var))
