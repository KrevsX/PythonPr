# -*- coding: utf-8 -*-
"""
Crear un programa que llene una matriz de 6x6 con las dos
diagonales con 1 y el resto con 0 como se muestra a continuación:
"""

matriz=[]

for i in range(6):
    for j in range(6):
        if i==0 and j==0:
            valor=1
            matriz.append(valor)
        elif i==0 and j==5:
            valor=1
            matriz.append(valor)
        elif i==1 and j==1:
            valor=1
            matriz.append(valor)
        elif i==1 and j==4:
            valor=1
            matriz.append(valor)
        elif i==2 and j==2:
            valor=1
            matriz.append(valor)
        elif i==2 and j==3:
            valor=1
            matriz.append(valor)
        elif i==3 and j==2:
            valor=1
            matriz.append(valor)
        elif i==3 and j==3:
            valor=1
            matriz.append(valor)
        elif i==4 and j==1:
            valor=1
            matriz.append(valor)
        elif i==4 and j==4:
            valor=1
            matriz.append(valor)
        elif i==5 and j==0:
            valor=1
            matriz.append(valor)
        elif i==5 and j==5:
            valor=1
            matriz.append(valor)
        else:
            valor=0
            matriz.append(valor)

print(matriz)
