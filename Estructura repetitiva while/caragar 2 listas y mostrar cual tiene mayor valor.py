# Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un
# mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", 
# "Lista 2 mayor", "Listas iguales")
# Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo"""

x = 1
y = 1
suma1 = 0
suma2 = 0

while x <=15:
    valor1 = int(input("Ingrese valor de la lista 1: "))
    suma1 = suma1 + valor1
    x=x+1
while y <=15:
    valor2 = int(input("Ingrese valor de la lista 2: "))
    suma2 = suma2 + valor2
    y=y+1
if suma1 > suma2:
    print("Lista 1 mayor")
else:
    if suma2 > suma1:
        print("Lista 2 mayor")
    else:   
        if suma1 == suma2:
            print("Listas iguales")
     
    

