from django.urls import path

from . import views

urlpatterns = [
    path('<int:customer_id>/', views.indexprestamo, name='indexprestamo'),
    path('<int:customer_id>/pedirprestamo', views.pedirprestamo, name='prestamos-pedirprestamo'),

    ]