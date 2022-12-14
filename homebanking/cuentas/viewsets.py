from django.contrib.auth.models import User
from rest_framework import  viewsets,status

from rest_framework.response import  Response
from rest_framework.permissions import AllowAny,IsAuthenticated

from cuentas.permissions import IsEmployee
from cuentas.serializers import *
from cuentas.models import Cliente, Cuenta, Prestamo, Direccion, Tarjeta, Sucursal,Empleado


# ViewSets define the view behavior.


class CuentaViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer

    def get_queryset(self):        #si el cliente entra a la lista de cuentas, le aparece su cuenta
        user = self.request.user
        try:
            cliente = Cliente.objects.get(user_id=user.id)
            return Cuenta.objects.filter(customer_id=cliente.customer_id)
        except:                    #"asumimos" que al no ser Cliente, va a ser empleado
            return Cuenta.objects.all()


class ClienteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get_queryset(self):             
        try:
            Empleado.objects.get(user_id = self.request.user.id)
            queryset = Cliente.objects.all()
            customer_id = self.request.query_params.get('customer_id')
            if customer_id is not None:
                queryset = queryset.filter(customer_id=customer_id)
            return queryset
        except:
            user = self.request.user
            return Cliente.objects.filter(user_id=user.id)


class PrestamoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def get_queryset(self):            
        queryset = Prestamo.objects.all()
        try:
            Empleado.objects.get(user_id = self.request.user.id)
            queryset = Prestamo.objects.all()
            branch_id = self.request.query_params.get('branch_id')
            if branch_id is not None:          
                branch_clientes = Cliente.objects.filter(branch_id=branch_id)
                queryset = queryset.filter(customer_id__in=branch_clientes)
            return queryset
        except:
            user = self.request.user
            cliente = Cliente.objects.get(user_id = user.id)
            return Prestamo.objects.filter(customer_id=cliente.customer_id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        monto = int(request.data.get('loan_total'))
        cliente = Cliente.objects.get(customer_id = request.data['customer'])
        cuenta = Cuenta.objects.get(customer_id = cliente.customer_id) 
        cuenta.balance = int(cuenta.balance) + monto
        cuenta.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
       
        instance = self.get_object()
        # cliente = Cliente.objects.get(customer_id = instance.customer)
        # cuenta = Cuenta.objects.get(customer_id = cliente.customer_id) 
        print(type(instance))
        # print(cliente)
        # print(cuenta)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)  

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ('create','destroy'):
            permission_classes = [IsEmployee]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]  


  

class DireccionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

    def get_queryset(self):        #si el cliente entra a la lista de cuentas, le aparece su cuenta
        user = self.request.user
        try:
            cliente = Cliente.objects.get(user_id=user.id)
            return Direccion.objects.filter(cliente=cliente.customer_id)
        except:
            return Direccion.objects.all()
    

class TarjetaViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer

    def get_queryset(self):        #permite filtrar la lista de tarjetas por customer_id         
        try:
            Empleado.objects.get(user_id = self.request.user.id)
            queryset = Tarjeta.objects.all()
            customer_id = self.request.query_params.get('customer_id')
            if customer_id is not None:          
                queryset = queryset.filter(cliente_id=customer_id)
            return queryset
        except:
            user = self.request.user
            cliente = Cliente.objects.get(user_id = user.id)
            return Tarjeta.objects.filter(cliente_id=cliente.customer_id)


class SucursalViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]

    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer



