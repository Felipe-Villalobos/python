# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un 
# programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran
# entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el 
# importe que gasta la empresa en sueldos al personal.

x = 1 
mayor100 = 0
mayor300 = 0
sueldot1 = 0
sueldot2 = 0
nempleados = int(input("Ingrese el nuero de empleados: "))

while x<=nempleados:
    sueldo = int(input("Ingrese sueldo empleado: "))
    if sueldo >=100 and sueldo<=300:
        mayor100 = mayor100+1
        sueldot1 = sueldot1 + sueldo
    else:
         if sueldo >300 and sueldo<=500:
            mayor300 = mayor300+1
            sueldot2 = sueldot2 + sueldo
    x=x+1
importe = sueldot1 + sueldot2
print(f"la cantidad de empleados que ganan entre 100 y 300 es: {mayor100}")
print(f"el total pagado a empleados que ganan entre 100 y 300 es: {sueldot1}")
print(f"la cantidad de empleados que ganan mas de 300  es: {mayor300}")
print(f"el total pagado a empleados que ganan mas de 300 es: {sueldot2}")