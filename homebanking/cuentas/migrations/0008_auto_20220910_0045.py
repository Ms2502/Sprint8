# Generated by Django 4.1 on 2022-09-09 15:41

from django.db import migrations
from django.contrib.auth.models import User
from django.apps import apps


def mix_empleado_user(apps,schema_editor):
    Empleado = apps.get_model("cuentas","Empleado")
    User = apps.get_model("auth","User")
    for e in Empleado.objects.all():
        #armamos las variables necesarias para crear el usuario
        username = f"{e.employee_name.lower()}{e.employee_surname.lower()}{str(e.employee_id)}"
        email = f"{username}@empleadoitbank.com.ar"
        password = "123456"
        #llamamos metodo de django para crear el usuario
        user = User.objects.create_user(username,email,password)
        user.first_name = e.employee_name
        user.last_name = e.employee_surname
        #asociamos usuario al cliente y guardamos
        e.user = user
        e.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0007_cliente_tipo_cliente'),
    ]

    operations = [
        migrations.RunPython(mix_empleado_user),
    ]