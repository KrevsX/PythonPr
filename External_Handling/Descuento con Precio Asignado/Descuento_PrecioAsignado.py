#Dar descuento del 60% al vender producto que no es fresco con precio Asignado.
 
from traitlets import Float


precioxUni = 3.50 
descuento = 0.6
 
prducto = int(input("Introduce el número de producto no fresco: "))

costo = prducto * precioxUni * (1 - descuento)
print("El costo de una producto fresco: " + Float(precioxUni) + "$")
print("El descuento por Producto no fresco: " + str(descuento * 100) + "%")
print("El total a pagar: " + str(round(costo, 2)) + "$")