#Realizar un programa que lea cuatro valores numéricos e informar su suma y promedio
import statistics

num1= int(input("ingrese el primer numero: "))
num2= int(input("ingrese el segundo numero: "))
num3= int(input("ingrese el tercer numero: "))
num4= int(input("ingrese el cuarto numero: "))

list = [num1,num2,num3,num4]
suma = sum(list)
promedio =statistics.mean(list)

print(f"La suma de los valores es: {suma}")
print(f"El promedio de los valores es: {promedio}")