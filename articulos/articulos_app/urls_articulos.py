from django.urls import path
from . import views

urlpatterns = [

    path('listado/', views.listar_articulos, name = 'lista_articulos'),
    path('hardware/', views.listar_hardware, name = 'lista_hardware' ),
    path('software/', views.listar_software, name = 'lista_software' ),
    
]