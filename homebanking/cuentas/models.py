# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User



class AuditoriaCuenta(models.Model):
    change_id = models.AutoField(primary_key=True)
    old_id = models.IntegerField(blank=True, null=True)
    new_id = models.IntegerField(blank=True, null=True)
    old_balance = models.IntegerField(blank=True, null=True)
    new_balance = models.IntegerField(blank=True, null=True)
    old_iban = models.TextField(blank=True, null=True)
    new_iban = models.TextField(blank=True, null=True)
    old_type = models.IntegerField(blank=True, null=True)
    new_type = models.IntegerField(blank=True, null=True)
    user_action = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auditoria_cuenta'


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    tipo_cliente = models.IntegerField(null =True, blank=True)

    user = models.OneToOneField(User,null =True, blank=True, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'cliente'

    def __str__(self):
        return f"{self.customer_name} {self.customer_surname}"


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(
        Cliente, 
        null =True, blank=True,
        on_delete=models.CASCADE, 
        db_column="customer_id",
        related_name="cuentas",
        )    
    balance = models.IntegerField()
    iban = models.TextField()
    tipo_cuenta = models.ForeignKey('TipoCuenta', models.DO_NOTHING, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'cuenta'

    def __str__(self):
        return f"{self.account_id}-{self.iban}"


class Direccion(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    calle = models.TextField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    ciudad = models.TextField(blank=True, null=True)
    provincia = models.TextField(blank=True, null=True)
    pais = models.TextField(blank=True, null=True)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
    empleado = models.ForeignKey('Empleado', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    user = models.OneToOneField(User,null =True, blank=True, on_delete=models.CASCADE)


    class Meta:
        managed = True
        db_table = 'empleado'


class MarcaTarjeta(models.Model):
    marca_id = models.AutoField(primary_key=True)
    marca_nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'marca_tarjeta'


class Movimientos(models.Model):
    movimiento_id = models.AutoField(primary_key=True, blank=True, null=False)
    account = models.ForeignKey(Cuenta, models.DO_NOTHING, blank=True, null=True)
    monto = models.IntegerField(blank=True, null=True)
    tipo_operacion = models.TextField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movimientos'


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'


class Tarjeta(models.Model):
    numero = models.TextField(primary_key=True)
    cvv = models.IntegerField(db_column='CVV')  # Field name made lowercase.
    fecha_otorgamiento = models.TextField()
    fecha_expiracion = models.TextField()
    credito_debito = models.TextField()
    marca = models.ForeignKey(MarcaTarjeta, models.DO_NOTHING)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tarjeta'


class TipoCliente(models.Model):
    tipo_cliente_id = models.AutoField(primary_key=True)
    tipo_cliente_nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cliente'


class TipoCuenta(models.Model):
    tipo_cuenta_id = models.AutoField(primary_key=True)
    tipo_cuenta_nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'
