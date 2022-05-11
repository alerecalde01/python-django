from django.db import models

class Articulo(models.Model):

    categorias = (
        ('Hard', 'Hardware'),
        ('Soft', 'Software'),
        ('Ins', 'Insumos'),
        ('Serv', 'Servicio'),
        ('Var', 'Varios')

    )

    codigo = models.CharField(max_length=8)
    descripcion = models.CharField(max_length = 120)
    precio = models.DecimalField(max_digits = 50, decimal_places = 2)
    categoria = models.CharField(max_length = 4, choices = categorias, default = 'x')


