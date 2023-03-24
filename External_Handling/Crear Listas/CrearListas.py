#creando listas...................
#datos = list()
#datos = []
datos =["hola",3.14,10, True, None]
print(type(datos))

#agregar valores a la lista.......
print(datos)
datos.append(4.55)
print(datos)
datos.append("hello")
print(datos)
var = "Xyz"
datos.insert(2, var)
datos.append("Xyz")
print(datos)

#borrar elementos
datos.pop(3)  #por indice
print(datos)
datos.remove("Xyz") #por valor
print(datos)

#impresiones de la lista
print(datos[4])
print(datos)
for i in range(len(datos)):
    print(datos[i])
    
#busqueda de registros
abuscar=None
for i in range(len(datos)):
     if datos[i]==abuscar:
         print("Encontrado: ",datos[i],"[",i,"]")

#odenado de lista
lista = [10,55,2,80,150,43,11,10]
lista.sort(reverse=True)
print(lista)
lista2 = ["tu", "hola", "estas", "como", "hoy"]
lista2.sort(key=len , reverse=False)
print(lista2)

#anidar listas
listaX = ["a","b","c"]
listaY = [listaX,"d"]

#recoriendo la listaY
#  imprimir    a b c d
print("\n\n")
for i in range(len(listaY)):
    if type(listaY[i])==list:
        for k in range(len(listaY[i])):
            print(listaY[i][k], end=" ")
    else:
        print(listaY[i], end=' ')
           
    
    


    



