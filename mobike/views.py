from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime

def hola(request):
    return HttpResponse("Hola mundo")

