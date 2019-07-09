from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from extended_settings.models import ExtentedSettings

def index(request):
    var = settings.APPLICATION_SENTENCE
    var2 = ExtentedSettings.get("title", '---')
    return HttpResponse("<html><body><h2>Welcome here!</h2><p>Configuration is '{}'</p><p>Title is '{}'</p></body></html>".format(var, var2))
