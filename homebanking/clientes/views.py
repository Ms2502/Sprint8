from django.shortcuts import HttpResponse,render
from django.contrib.auth.decorators import login_required

# Create your views here.

from cuentas.models import *

@login_required(login_url="/login/") 
def detail(request,customer_id):
    cuenta = Cuenta.objects.get(customer_id=customer_id)
    movimientos= Movimientos.objects.filter(account_id = cuenta.account_id)
      

    prestamos= Prestamo.objects.filter(customer_id = customer_id)    
  
    context = dict(cuenta=cuenta,movimientos=movimientos,prestamos=prestamos)
    return render(request,"clientes/index.html",context)






# @login_required(login_url="/login/") 
# def index1(request):
#     listado_clientes = Cliente.objects.all()
#     context = dict(listado_clientes=listado_clientes)
#     return render(request,"clientes/index1.html",context)

# @login_required(login_url="/login/") 
# def detail(request,customer_id):
#     cliente = Cliente.objects.get(customer_id=customer_id)
#     context = dict(cliente=cliente)

#     return render(request,"clientes/index.html",context)

