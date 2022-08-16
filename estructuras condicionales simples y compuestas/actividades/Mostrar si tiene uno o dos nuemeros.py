#Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando 
# si el número tiene uno o dos dígitos.
#(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)

num = int(input("Ingrese un numero entre 1 y 99 "))

if num >= 10:

    print("El número tiene 2 digitos")

else:

    print("El número tiene 1 digito")
