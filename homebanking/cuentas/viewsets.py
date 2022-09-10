from django.contrib.auth.models import User
from rest_framework import  viewsets
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated

from cuentas.serializers import *
from cuentas.models import Cuenta

#f34f640d79d8e44b02e39d4e284e5b66e62ea7ab> username="helenjordan17" ##############    1h06m

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer

    # def get_permissions(self):
    #     """
    #     Instantiates and returns the list of permissions that this view requires.
    #     """
    #     if self.action == 'list':
    #         permission_classes = [AllowAny]
    #     else:
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        cliente = Cliente.objects.get(user_id = user.id)
        return Cuenta.objects.filter(customer_id=cliente.customer_id)

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get_queryset(self):
        user = self.request.user
        return Cliente.objects.filter(user_id=user.id)

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def get_queryset(self):
        user = self.request.user
        cliente = Cliente.objects.get(user_id = user.id)
        return Prestamo.objects.filter(customer_id=cliente.customer_id)

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class TarjetaViewSet(viewsets.ModelViewSet):
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer

class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer



