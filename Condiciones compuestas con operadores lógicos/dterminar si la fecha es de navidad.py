#Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha
#  fecha corresponde a Navidad.

dia=int(input("Ingrese nro de día:"))
mes=int(input("Ingrese nro de mes:"))
año=int(input("Ingrese nro de año:"))

if dia == 25 and mes ==12:
    print("La fecha corresponde a Navidad")
else:
    print("La fecha NO corresponde a Navidad")