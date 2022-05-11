from re import A
from django.shortcuts import render, HttpResponse
from .models import Articulo

# Create your views here.

def listar_articulos(request):

    lista_articulos = Articulo.objects.all()
    articulo = {'articulos': lista_articulos}

    return render(request, 'articulos_app/lista.html', articulo)


def listar_hardware(request):

    hardware = {}

    if Articulo.categoria == "Hardware":
        hardware['codigo'] = Articulo.codigo
        hardware['descripcion'] = Articulo.descripcion

    return render(request, 'articulos_app/hardware.html', hardware) 
         
