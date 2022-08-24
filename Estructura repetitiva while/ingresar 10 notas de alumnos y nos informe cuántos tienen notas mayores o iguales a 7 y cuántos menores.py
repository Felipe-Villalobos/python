#Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen 
# notas mayores o iguales a 7 y cuántos menores


x = 1
n = 0
cantalumnos = int(input("ingrese la cantidad de alumnos  a evaluar: "))
while x<=cantalumnos:
    nota = int (input("Ingrese la nota: ")) 
    if nota >=7:
        n= n+1
    x=x+1
print("La cantidad de alumnos que tienen notas mayores a 7 es: ")
print(n)
