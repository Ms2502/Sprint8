# Sprint 8

Admin:
user = admin
password = contraseña

Empleado:
user = danielramsey500
password = 123456

Cliente:
algunos users = (tashyarichards451, cherokeewilliams8, kimosborn304, mosesgreer1)
password = 123456

Los clientes solo pueden ver su informacion, los empleados pueden ver toda la informacion, y crear/borrar prestamos.


 - http://localhost:8000/api/ 

 - /api/clientes/
 - /api/cuentas/
 - /api/prestamos/
 - /api/direcciones/
 - /api/tarjetas/
 - /api/sucursales/

 - /api/clientes/?customer_id=23
 - /api/prestamos/?branch_id=23
 - /api/tarjetas/?customer_id=14


 OBTENER DATOS DE UN CLIENTE X
Un cliente autenticado puede consultar sus propios datos

http://localhost:8000/api/clientes

 OBTENER SALDO DE CUENTA DE UN CLIENTE X
Un cliente autenticado puede obtener el tipo de cuenta y su saldo

http://localhost:8000/api/cuentas

 OBTENER MONTO DE PRESTAMOS DE UNA SUCURSAL X
Un empleado autenticado puede obtener el listado de préstamos otorgados de
una sucursal determinada.

http://localhost:8000/api/prestamos?branch_id=3 

 OBTENER TARJETAS ASOCIADAS A UN CLIENTE X
Un empleado autenticado puede obtener el listado de tarjetas de crédito de un
cliente determinado

http://localhost:8000/api/tarjetas?customer_id=3 


 OBTENER MONTO DE PRESTAMOS DE UN CLIENTE X
Un cliente autenticado puede obtener el tipo de préstamo y total del mismo

http://localhost:8000/api/prestamos

 GENERAR UNA SOLICITUD DE PRESTAMO PARA UN CLIENTE
Un empleado autenticado puede solicitar un préstamo para un cliente, registrado
el mismo y acreditando el saldo en su cuenta

http://localhost:8000/api/prestamos/440/ (POST)

 ANULAR SOLICITUD DE PRESTAMO DE CLIENTE
Un empleado autenticado puede anular un préstamo para un cliente, revirtiendo
el monto correspondiente

http://localhost:8000/api/prestamos/440/ (DELETE)


 MODIFICAR DIRECCION DE UN CLIENTE
El propio cliente autenticado o un empleado puede modificar las direcciones. 

http://localhost:8000/api/direcciones/3/ (PATCH)

 LISTADO DE TODAS LAS SUCURSALES X
Un endpoint público que devuelve el listado todas las sucursales con la
información correspondiente.

http://localhost:8000/api/sucursales/