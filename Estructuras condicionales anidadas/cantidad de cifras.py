#Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y 
# muestre un mensaje indicando si tiene 1, 2, o 3 cifras. 
# Mostrar un mensaje de error si el número de cifras es mayor.

num = int(input("Ingrese un numero entre 1 y 999: "))

if num < 0:
    print("Error en la entrada de datos")
else:    
    if num < 10:
            print("El numero tiene 1 cifra")
    else:
        if num < 100:
             print("El nuemro tiene 2 cifras")
        else:
            if num < 1000:
                print("El numero tiene 3 cifras")
            else:
                print("Error en la entrada de datos")


