from rest_framework import permissions
from cuentas.models import *

class IsEmployee(permissions.BasePermission):
    message = 'Debe logearse como empleado para acceder a esta funcion.'

    def has_permission(self, request, view):
        user = request.user
        try:
            Cliente.objects.get(user_id=user.id)
            return False
        except:
            pass
        try:
            Empleado.objects.get(user_id=user.id)
            return True
        except:
            pass



# def es_empleado(request):
#     user = request.user
#     try:
#         Cliente.objects.get(user_id=user.id)
#         return False
#     except:
#         pass
#     try:
#         Empleado.objects.get(user_id=user.id)
#         return True
#     except:
#         pass




