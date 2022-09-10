from msilib.schema import Error
from rest_framework import permissions
from cuentas.models import * 

# def empleado(request):
#     try:
#         empleado = Empleado.objects.get(user_id=request.user.id)
#         print (empleado)
#         if empleado in Empleado.objects.all():
#             return True
#             print("es empleado")
#     except Error:
#         return False

# class EsEmpleado(permissions.BasePermission):
#     message = 'Solo disponible para empleados,intente iniciando sesión.'

#     def has_permission(self, request, view):
#         request.user and empleado(request)


