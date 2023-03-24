#Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre
# por pantalla una serie con los datos de las ventas indexada por los años, antes y después
# de aplicarles un descuento del 10%.

import pandas as pd

inicio = int(input('Introduce el año inicial: '))
fin = int(input('Introduce el año final: '))
ventas = {}
for i in range(inicio, fin+1):
    ventas[i] = float(input('Introduce las ventas del año ' + str(i) +': '))
ventas = pd.Series(ventas)
print('Ventas\n', ventas)
print('Ventas con descuento\n', ventas*0.9)