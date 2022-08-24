#Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de 
# las personas.

x = 1
suma = 0
cantpersonas = int(input(" Ingrese numero de personas: "))
while x<=cantpersonas:
    estatura = float(input("ingrese la estatura: "))
    suma = suma + estatura
    x=x+1
promedio = suma / cantpersonas
print (f"el promedio de estatura de las {cantpersonas} personas es:")
print(f'{promedio:.2f}')