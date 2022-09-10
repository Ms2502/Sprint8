from django.contrib import admin

from cuentas.models import Cliente,Cuenta

# Register your models here.

admin.site.register(Cliente)

# class CuentaAdmin(admin.ModelAdmin):
#     list_display = ('account_id','cliente')

admin.site.register(Cuenta)


