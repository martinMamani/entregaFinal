from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def inicio(request):
    name = '<h1>inicio perfil </h1>'
    return HttpResponse(name)