from django.db import models

# Create your models here.

class Producto(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    url = models.ImageField()