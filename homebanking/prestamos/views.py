from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

from cuentas.models import Cliente, Prestamo, Cuenta
from datetime import datetime

@login_required(login_url="/login/") 
def indexprestamo(request,customer_id):
    cuenta = Cuenta.objects.get(customer_id=customer_id)
    prestamos= Prestamo.objects.filter(customer_id = customer_id)    
    context = dict(prestamos=prestamos,cuenta=cuenta)
    return render(request,"prestamos/prestamos.html",context)

@login_required(login_url="/login/") 
def pedirprestamo(request,customer_id):
    valor = int(request.POST.get("valor"))
    tipoprestamo = request.POST.get("loantype")
    fechaprestamo = datetime.now().strftime("%d-%m-%Y")
    tipocliente = Cliente.objects.get(customer_id=customer_id).tipo_cliente

    if tipocliente == 1: #classic
        valor_max = 100000
        if valor > valor_max:
            error = f"Monto maximo excedido (monto maximo permitido: {valor_max})"
            pass
        else:
            print("transaccion exitosa")
            success = "Prestamo procesado con exito"
            Prestamo.objects.create(customer_id=customer_id, loan_total = valor,loan_type = tipoprestamo, loan_date = fechaprestamo)

    elif tipocliente == 2: #gold
        valor_max = 300000
        if valor > valor_max:
            error = f"Monto maximo excedido (monto maximo permitido: {valor_max})"
            pass
        else:
            print("transaccion exitosa")
            success = "Prestamo procesado con exito"

            Prestamo.objects.create(customer_id=customer_id, loan_total = valor,loan_type = tipoprestamo, loan_date = fechaprestamo)

    elif tipocliente == 3: #black
        valor_max = 500000
        if valor > valor_max:
            error = f"Monto maximo excedido (monto maximo permitido: {valor_max})"
            pass
        else:
            print("transaccion exitosa")
            success = "Prestamo procesado con exito"
            Prestamo.objects.create(customer_id=customer_id, loan_total = valor,loan_type = tipoprestamo, loan_date = fechaprestamo)

    if 'error' in locals(): print(error)

    return redirect("indexprestamo",customer_id)
    
