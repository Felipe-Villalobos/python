# Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores 
# fueron pares y cuántos impares.
# Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el
# esto de la división de dos valores, por ejemplo 11%2 retorna un 1):

from sqlite3 import paramstyle


x = 1
par = 0
impar = 0
cantnum = int(input("Ingrese la cantidad de numeros a clasificar: "))

while x<=cantnum:
    num = int(input("Ingrese el numero: "))
    if num % 2 == 0:
        par = par+1
    else:
        impar = impar+1
    x=x+1
print(f"La cantidad de numeros pares es: {par}")
print(f"La cantidad de numeros impares es: {impar}")


