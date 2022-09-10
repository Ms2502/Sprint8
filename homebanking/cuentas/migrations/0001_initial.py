# Generated by Django 4.1 on 2022-08-30 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditoriaCuenta',
            fields=[
                ('change_id', models.AutoField(primary_key=True, serialize=False)),
                ('old_id', models.IntegerField(blank=True, null=True)),
                ('new_id', models.IntegerField(blank=True, null=True)),
                ('old_balance', models.IntegerField(blank=True, null=True)),
                ('new_balance', models.IntegerField(blank=True, null=True)),
                ('old_iban', models.TextField(blank=True, null=True)),
                ('new_iban', models.TextField(blank=True, null=True)),
                ('old_type', models.IntegerField(blank=True, null=True)),
                ('new_type', models.IntegerField(blank=True, null=True)),
                ('user_action', models.TextField(blank=True, null=True)),
                ('created_at', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'auditoria_cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('direccion_id', models.AutoField(primary_key=True, serialize=False)),
                ('calle', models.TextField(blank=True, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('ciudad', models.TextField(blank=True, null=True)),
                ('provincia', models.TextField(blank=True, null=True)),
                ('pais', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'direccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.TextField()),
                ('employee_surname', models.TextField()),
                ('employee_hire_date', models.TextField()),
                ('employee_dni', models.TextField(db_column='employee_DNI')),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MarcaTarjeta',
            fields=[
                ('marca_id', models.AutoField(primary_key=True, serialize=False)),
                ('marca_nombre', models.TextField()),
            ],
            options={
                'db_table': 'marca_tarjeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('movimiento_id', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.IntegerField(blank=True, null=True)),
                ('tipo_operacion', models.TextField(blank=True, null=True)),
                ('hora', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movimientos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_type', models.TextField()),
                ('loan_date', models.TextField()),
                ('loan_total', models.IntegerField()),
                ('customer_id', models.IntegerField()),
            ],
            options={
                'db_table': 'prestamo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_number', models.BinaryField()),
                ('branch_name', models.TextField()),
                ('branch_address_id', models.IntegerField()),
            ],
            options={
                'db_table': 'sucursal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('numero', models.AutoField(primary_key=True, serialize=False)),
                ('cvv', models.IntegerField(db_column='CVV')),
                ('fecha_otorgamiento', models.TextField()),
                ('fecha_expiracion', models.TextField()),
                ('credito_debito', models.TextField()),
            ],
            options={
                'db_table': 'tarjeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('tipo_cliente_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_cliente_nombre', models.TextField()),
            ],
            options={
                'db_table': 'tipo_cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoCuenta',
            fields=[
                ('tipo_cuenta_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_cuenta_nombre', models.TextField()),
            ],
            options={
                'db_table': 'tipo_cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.TextField()),
                ('customer_surname', models.TextField()),
                ('customer_dni', models.TextField(db_column='customer_DNI')),
                ('dob', models.TextField(blank=True, null=True)),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'cliente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('iban', models.TextField()),
                ('tipo_cuenta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuentas.tipocuenta')),
            ],
            options={
                'db_table': 'cuenta',
                'managed': True,
            },
        ),
    ]