#Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, 
# negativo o nulo (es decir cero)


num = int(input("ingrese el numero: "))

if num == 0:
     print("el numero es nulo")
else:
    if num > 0:
        print("el numero es positivo")
    else:
        print("el numero es negativo")