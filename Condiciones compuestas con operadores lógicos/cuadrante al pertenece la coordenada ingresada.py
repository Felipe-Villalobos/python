#Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir
#  dos valores enteros x e y (distintos a cero).
#Posteriormente imprimir en pantalla en que 
# #cuadrante se ubica dicho punto:
# 1º Cuadrante si x > 0 Y y > 0 
# 2º Cuadrante: x < 0 Y y > 0
# 3º Cuadrante: x < 0 Y y < 0
# 4º Cuadrante: x > 0 Y y < 0

x = int(input("Ingrese el valor correspondiente a X: "))
y = int(input("Ingrese el valor correspondiente a Y: "))

if x > 0  and y > 0:
    print("La coordenada ingresada pertenece al 1º Cuadrante")
else:
    if x < 0  and y > 0:
        print("La coordenada ingresada pertenece al 2º Cuadrante")
    else:
        if x < 0  and y < 0:
            print("La coordenada ingresada pertenece al 3º Cuadrante")
        else:
            print("La coordenada ingresada pertenece al 4º Cuadrante")
