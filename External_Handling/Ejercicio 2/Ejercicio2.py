# Para mostrar productos, precio por cada unidad, subtotal y precio total:
print("\nPara mostrar productos, precio por cada unidad, subtotal y precio total:")
total = 0
productos=[]
while True:
    producto = input("Nombre Producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "),"$")
    subtotal=round(cantidad * precio, 2)
    total += subtotal
    productos.append((producto+" --> Cantidad: "+str(cantidad)+ 
                      " Unidades --> Precio C/U: "+str(precio)+ 
                      " Dolares --> Subtotal: "+str(subtotal)+ 
                      " $ Dolares"))
    continuar = input("Presionar X para calcular o enter para continuar: ")
    if continuar == "X":
        print("Productos: ")
        [print("-",p) for p in productos]
        print("Precio total:", round(total,2),"$ Dolares")
        break

#--------------- Alternativa con Diccionario----

# print("\nAlternativa con Diccionario----)
# total = 0
# productos={}
# while True:
#     producto = input("Nombre Producto: ")
#     cantidad = int(input("Cantidad: "))
#     precio = float(input("Precio: "),"$")
#     subtotal=round(cantidad * precio, 2)
#     total += subtotal
#     productos[producto]=(cantidad,precio,subtotal)
#     continuar = input("Presionar X para calcular o enter para continuar: ")
#     if continuar == "X":
#         print("Productos: ")
#         [print("-",p,"--> Cantidad:",productos[p][0],
#                "Unidades --> Precio C/U:",productos[p][2],
#                "$ Dolares --> Subtotal:",productos[p][2],
#                "$ Doalres")
#          for p in productos]
#         #Alternativa para mostrar los detalles
#         print("Alternativa 1  para Mostar Detalles: ")
#         print("Precio total:", round(total, 2), "pesos")
#         print("Alternativa 2  para Mostar Detalles: ")
#         print("Precio total:", round(sum(productos[p][2] for p in productos),2), "pesos")        
#         break