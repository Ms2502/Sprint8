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
        fields = ['cliente','tipo_cuenta', 'balance']


class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = "__all__"


class PrestamoSerializer(serializers.ModelSerializer):
    sucursal = serializers.SerializerMethodField()
    def get_sucursal(self,obj):
        return Sucursal.objects.get(branch_id=obj.customer.branch_id).branch_name
    
    branch_id = serializers.SerializerMethodField()
    def get_branch_id(self,obj):
        return Sucursal.objects.get(branch_id=obj.customer.branch_id).branch_id

    class Meta:
        model = Prestamo
        fields = "__all__"


class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ["direccion_id","calle","numero","ciudad","provincia","pais"]


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = "__all__"
