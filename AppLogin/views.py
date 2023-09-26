from django.shortcuts import render


from django.http import HttpResponse

# Create your views here.
def inicio(request):
    name = '<h1>inicio login </h1>'
    return HttpResponse(name)