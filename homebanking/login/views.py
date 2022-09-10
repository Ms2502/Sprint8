from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout

# Create your views here.

def index(request):
    return render(request,"login/index.html") #vendria a ser como la "landing page"

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        cus_id = user.cliente.customer_id
        if user is  None:
            return render(request, "login/login.html")
        else:
            login(request,user)
            return redirect("clientes-detail",cus_id) #redirige aca cuando el usuario se logea correctamente
    else:
        return render(
            request, 
            "login/login.html",
            context=dict(error="Usuario o contraseña invalidos") #hay que arreglar esto
            )

def logout_view(request):
    logout(request)
    return redirect("login")