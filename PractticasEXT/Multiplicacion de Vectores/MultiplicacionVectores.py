print("****************************************")
print("**** Multiplicacion de vectores 3x3 ****")
print("****************************************")

Vector1 = []
Vector2 = []
VectorR = []


for i in range (1,3,1):
    a = str(i)
    x = int(input("Ingrese el valor de la componente x del vector "+a+": "))
    y = int(input("Ingrese el valor de la componente y del vector "+a+": "))
    z = int(input("Ingrese el valor de la componente z del vector "+a+": "))
    if (i == 1):
        Vector1.insert(0,x)
        Vector1.insert(1,y)
        Vector1.insert(2,z)
    elif (i == 2):
        Vector2.insert(0,x)
        Vector2.insert(1,y)
        Vector2.insert(2,z)
xr = Vector1[0]*Vector2[0]
yr = Vector1[1]*Vector2[1]
zr = Vector1[2]*Vector2[2]
VectorR.insert(0,xr)
VectorR.insert(1,yr)
VectorR.insert(2,zr)
print("**********************************")
print("Vector 1: ", Vector1)
print("**********************************")
print("Vector 2: ", Vector2)
print("**********************************")
print("El vector resultante es: ", VectorR)
print("**********************************")
