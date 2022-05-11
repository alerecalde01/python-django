from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Articulo

# Create your views here.

def listar_articulos(request):

    lista_articulos = Articulo.objects.all()
    articulo = {'articulos': lista_articulos}

    return render(request, 'articulos_app/lista.html', articulo)


def listar_hardware(request):

    cat = Articulo.objects.filter(categoria="Hard")
    articulo = {'categorias': cat}

    return render(request, 'articulos_app/hardware.html', articulo)
    
    
def listar_software(request):

    cat = Articulo.objects.filter(categoria="Soft")
    articulo = {'categorias': cat}

    return render(request, 'articulos_app/software.html', articulo)
    
         
