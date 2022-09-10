# Generated by Django 4.1 on 2022-08-30 18:42

from django.db import migrations
from django.contrib.auth.models import User
from django.apps import apps


def mix_cliente_user(apps,schema_editor):
    Cliente = apps.get_model("cuentas","Cliente")
    User = apps.get_model("auth","User")
    for c in Cliente.objects.all():
        #armamos las variables necesarias para crear el ususario
        username = f"{c.customer_name.lower()}{c.customer_surname.lower()}{str(c.customer_id)}"
        email = f"{username}@itbank.com.ar"
        password = "123456"
        #llamamos metodo de django para crear el usuario
        user = User.objects.create_user(username,email,password)
        user.first_name = c.customer_name
        user.last_name = c.customer_surname
        #asociamos usuario al cliente y guardamos
        c.user = user
        c.save()

class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0003_cliente_user'),
    ]

    operations = [
        migrations.RunPython(mix_cliente_user),
    ]