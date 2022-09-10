from django.urls import path, include
from rest_framework import routers

from .viewsets import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'cuentas', CuentaViewSet)
router.register(r'prestamos', PrestamoViewSet)
router.register(r'direcciones', DireccionViewSet)
router.register(r'tarjetas', TarjetaViewSet)
router.register(r'sucursales', SucursalViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]