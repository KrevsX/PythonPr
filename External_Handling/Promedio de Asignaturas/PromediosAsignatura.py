 # -*- coding: utf-8 -*-
"""
Crear un programa que permita registra las notas
obtenidas en Matematica, Sociales y Ciencias
para un grupo de N estudiantes, 
el programa debe permitir:
    * ingresar notas en base a carnet
    * encontrar informacion de un estudiante
    *calcular promedios por asignatura
"""
estudiantes=[]
opcion=0
while opcion!=4:
    print("\n\n\n\n")
    print("1) Ingreso de notas")
    print("2) Buscar estudiante")
    print("3) Calculo de promedios por asignatura")
    print("4) Salir")
    opcion=int(input("Opcion: "))
    if opcion==1:
        carnet= input("Carnet de estudiante: ")
        mate = float(input("Mate: "))
        soc = float(input("Sociales: "))
        cc = float(input("Ciencia: "))
        registro=[carnet, mate, soc, cc]
        estudiantes.append(registro)
        input()
    elif opcion==2:
        if len(estudiantes)<=0:
            print("No hay registros aun...")
        else:
            encontrado=False
            carnet=input("Carnet de estudiante: ")
            for i in range(len(estudiantes)):
                if estudiantes[i][0]==carnet:
                    encontrado=True
                    print("Carnet: ", estudiantes[i][0])
                    print("Mate: ", estudiantes[i][1])
                    print("Sociales: ", estudiantes[i][2])
                    print("Ciencias: ", estudiantes[i][3])
            if not encontrado:
                print("carnet no encontrado....")  
        input()
        
    elif opcion==3:
        cuantos =len(estudiantes) 
        promMate=0
        promSoc=0
        promCC=0
        for i in range(cuantos):
            promMate += estudiantes[i][1]
            promSoc += estudiantes[i][2]
            promCC += estudiantes[i][3]
        promMate /= cuantos
        promSoc /=cuantos
        promCC /= cuantos
        print("Promedio Mate: ", promMate)
        print("Promedio Sociales: ", promSoc)
        print("Promedio Ciencias: ", promCC)
        input()
    elif opcion==4:
        print("programa terminado...")
    else:
        print("Opcion invalida")
        input()









