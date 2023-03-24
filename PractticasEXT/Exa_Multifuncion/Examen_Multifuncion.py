"""
Se le ha contactado a usted para que pueda crear un 
programa que resuelva la problemática de una empresa,
 esta empresa vende Vehículos usados, es una empresa nueva y
 necesita un programa en el que pueda registrar los vehículos ,
 y por cada vehiculo se debe registrar:
- Identificador único o código (ejemplo: 101022 son 6 dígitos de tipo str)
- Marca (ejemplo: Honda, Ford, Mazda, Hyundai, etc)
- Modelo (ejemplo: Sedan, Coupe, PickUp, etc)
- Año del vehiculo
- Precio de compra del vehiculo
- Precio de venta del producto (siempre será el 35% sobre el valor del costo)

El programa debe permitir:
- Ingresar registros de vehículos (20%)
- Buscar vehiculo por Código (esto mostrará el detalle de cada producto) (20%)
- Listar vehiculos por marca (listará todos los vehiculos que sean de la misma marca) (20%)
- Calcular inversión de inventario (es la suma de todos los precios de compra ) (20%)
- Detallar cuantos vehículos son de un modelo específico (ejemplo, buscamos “sedan” 
y aparecerá el listado de todos los vehículos sedan, ya sean de diferentes marcas) (20%)
- Una opción para salir del programa

"""

Vehiculos=[]
opcion=0
while opcion!=6:
    print("\n\n\n\n")
    print("ELIJA SU ACCION:")
    print("1).Ingresar registro de vehiculos")
    print("2).Buscar vehiculo por Código")
    print("3).Listar vehiculos por marca")
    print("4).Calcular inversión de inventario")
    print("5).Detallar cuantos vehículos son de un modelo específico")
    print("6).Salir del Programa...")
    opcion=int(input("Opcion: "))
    if opcion==1:
        Codigo=input("Identificador único o código:")
        Marca=input("Marca del Vehiculo:")
        Modelo=input("Modelo del Vehiculo:")
        Año=input("Año del Vehiculo:")
        PrecioI=float(input("Precio de Compra del Vehiculo en Dolares:"))
        PrecioV=(PrecioI*0.35)+PrecioI
        print("Precio para la venta:",PrecioV)
        registro=[Codigo,Marca,Modelo,Año,PrecioI,PrecioV]
        Vehiculos.append(registro)
        input()
    elif opcion==2:
        if len(Vehiculos)<=0:
             print("No hay registro de Vehiculos...")
        else:
            Codigo=input("Identificador único o código:")
            encontrado=False
            for i in range(len(Vehiculos)):
                if Vehiculos[i][0]==Codigo:
                    encontrado=True
                    print("INFORMACION DEL VEHICULO")
                    print("Codigo:",Vehiculos[i][0])
                    print("Marca:",Vehiculos[i][1])
                    print("Modelo:",Vehiculos[i][2])
                    print("Año:",Vehiculos[i][3])
                    print("Precio de Costo:",Vehiculos[i][4])
                    print("Precio de Venta:",Vehiculos[i][5])
                if not encontrado:
                    print("Codigo no encontrado...")
                    input()
    elif opcion==3:
        if len(Vehiculos)<=0:
             print("No hay registro de Vehiculos...")
        else:
            Marca=input("Marca que desea consultar:")
            encontrado=False
            for i in range(len(Vehiculos)):
                if Vehiculos[i][1]==Marca:
                    encontrado=True
                    print("INFORMACION DEL VEHICULO")
                    print("Codigo:",Vehiculos[i][0])
                    print("Marca:",Vehiculos[i][1])
                    print("Modelo:",Vehiculos[i][2])
                    print("Año:",Vehiculos[i][3])
                    print("Precio de Costo:",Vehiculos[i][4])
                    print("Precio de Venta:",Vehiculos[i][5])
                    print("\n\n\n\n")
                if not encontrado:
                    print("Marca no encontrado...")
                    input()
    elif opcion==4:
        sumatotal=len(Vehiculos)
        invtotal=0
        if len(Vehiculos)<=0:
            print("No hay registros....")
            print("\n\n\n\n")
            encontrado=False
            for i in range ((sumatotal)):
                invtotal += Vehiculos[i][4]
                print("Inversion Genereal: ", invtotal)
                input()
            
    
        
        