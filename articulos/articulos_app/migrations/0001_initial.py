# Generated by Django 4.0.4 on 2022-05-11 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8)),
                ('descripcion', models.CharField(max_length=120)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=50)),
                ('categoria', models.CharField(choices=[('Hard', 'Hardware'), ('Soft', 'Softwares'), ('Ins', 'Insumos'), ('Serv', 'Servicio'), ('Var', 'Varios')], default='x', max_length=4)),
            ],
        ),
    ]