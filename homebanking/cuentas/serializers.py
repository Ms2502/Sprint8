from rest_framework import serializers
from django.contrib.auth.models import User

from cuentas.models import Cliente, Cuenta, Prestamo, Direccion, Tarjeta, Sucursal


# Serializers define the API representation.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"   

class CuentaSerializer(serializers.ModelSerializer):
    cliente = serializers.SerializerMethodField()
    def get_cliente(self, obj):
        return obj.customer_id.customer_name +" "+ obj.customer_id.customer_surname if obj.customer_id else ""
    
    tipo_cuenta= serializers.SerializerMethodField()
    def get_tipo_cuenta(self,obj):
        return obj.tipo_cuenta.tipo_cuenta_nombre

    class Meta:
        model = Cuenta
        fields = ['account_id', 'cliente', 'iban', 'tipo_cuenta', 'balance']

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = "__all__"

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = "__all__"

class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = "__all__"

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = "__all__"
