#Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos

num1=int(input("Ingrese primer numero:"))
num2=int(input("Ingrese segunda numero:"))
num3=int(input("Ingrese tercer numero:"))

if num1 > num2:
    if num1 > num3:
        print("el numero mayor es:")
        print(num1)
    else:
        print("el numero mayor es:")
        print(num3)
else:
    if num2 > num1:
        if num2 > num3:
            print("el numero mayor es:")
            print(num2)
        else:
            print("el numero mayor es:")
            print(num3)


