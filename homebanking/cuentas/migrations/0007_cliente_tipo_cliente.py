# Generated by Django 4.1 on 2022-09-10 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0006_cliente_tipo_cliente_empleado_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='tipo_cliente',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
