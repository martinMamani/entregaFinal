from django.shortcuts import render

from .models import Producto

# Create your views here.
def inicio(request):
    return render(request,"AppIndumentaria/plantilla.html")


def productos(request):
    productos = Producto.objects.all()
    return render(request,"AppIndumentaria/productos.html",{"productos":productos})