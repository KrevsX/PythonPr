# -*- coding: utf-8 -*-
"""
Created on Sun May 22 16:46:31 2022

@author: Josue Dominguez, Kevin Alas, Ivan Magana, Carlos Fuentes
"""
empleados={
            "codigoempleados":[],
            "nombreempleados":[],
            "sueldomensual":[],
            "numeroISSS":[],
            "numeroafp":[],
            "SAR":[],
            "renta":[],
            "isss":[],
            "afp":[],
            "sueldoneto":[]
            }

continuar=True

while continuar:
    print("**********************Los necesitados**********************************************")
    print("Digite el proceso que desea realizar")
    print("1)AGREGAR UN NUEVO EMPLEADO")
    print("2)MODIFICAR DATOS DE UN EMPLEADO")
    print("3)MOSTRAR PLANTILLA ORDENADA POR NOMBRE DE EMPLEADO")
    print("4)SALIR")
    print("*****************************************************")
#Validacion de las opciones----------------------------------------------------------------------------------
    testopcion=True
    opcion=input("Digite la opcion que desea realizar: ")
    while testopcion:
        try:
            opcion=int(opcion)
            testopcion=False
        except:
            opcion=input("No se admiten letras. Entre el digito de la opcion que desea realizar: ")
#Codigo de empleados----------------------------------------------------------------------------------    
    if opcion==1:
        codigoempleado=input("Ingrese el codigo del empleado: ")
        while not (codigoempleado.isnumeric() and len(codigoempleado)==6):
            codigoempleado=input("Ingrese el codigo del empleado sin letras y de 6 digitos: ")
        if len(empleados["codigoempleados"])==0:
            empleados["codigoempleados"].append(codigoempleado)
        elif len(empleados["codigoempleados"])!=0:
            if codigoempleado in empleados["codigoempleados"]:
                repetido=True
                while repetido:
                    codigoempleado=input("Codigo repetido. Ingrese uno nuevo: ")
                    while not (codigoempleado.isnumeric() and len(codigoempleado)==6):
                        codigoempleado=input("Ingrese el codigo del empleado sin letras y de 6 digitos: ")
                    if codigoempleado in empleados["codigoempleados"]:
                        repetido=True
                    else:
                        repetido=False
                        empleados["codigoempleados"].append(codigoempleado)
            else:
                empleados["codigoempleados"].append(codigoempleado)
#Nombres---------------------------------------------------------------------------------- 
        nombre=input("Nombre completo del empleado: ").lstrip()
        if any(chr.isdigit() for chr in nombre)==True:
            nombreincorrecto=True
            while nombreincorrecto:
                nombre=input("El nombre contiene numeros. Vuelvalo a ingresar: ").lstrip()
                if any(chr.isdigit() for chr in nombre)==True:
                    nombreincorrecto=True
                else:
                    empleados["nombreempleados"].append(nombre)
                    nombreincorrecto=False
        else:
            empleados["nombreempleados"].append(nombre)
#Sueldo y renta----------------------------------------------------------------------------------         
        testsueldo=True
        sueldo=input("Sueldo mensual del empleado: $")
        while testsueldo:
            try:
                sueldo=float(sueldo)
                testsueldo=False
            except:
                sueldo=input("Ingrese solo numeros para el sueldo mensual del empleado: $")
        if sueldo<=500:
            renta=0
            empleados["renta"].append(renta)
        elif sueldo>500 and sueldo<=1000:
            renta=round(sueldo*0.10)
            empleados["renta"].append(renta)
        elif sueldo>1000:
            renta=round(sueldo*0.20)
            empleados["renta"].append(renta)
        empleados["sueldomensual"].append(sueldo)
#Numero ISSS---------------------------------------------------------------------------------
        nisss=input("Ingrese numero del ISSS: ")
        while not (nisss.isnumeric() and len(nisss)==6):
            nisss=input("Ingrese el numero de ISSS sin letras y de 6 digitos: ")
        if len(empleados["numeroISSS"])==0:
            empleados["numeroISSS"].append(nisss)
        elif len(empleados["numeroISSS"])!=0:
            if nisss in empleados["numeroISSS"]:
                repetido=True
                while repetido:
                    nisss=input("numero de ISSS repetido. Ingrese uno nuevo: ")
                    while not (nisss.isnumeric() and len(nisss)==6):
                        nisss=input("Digite solo numeros y que contenga 6 digitos. Ingrese uno nuevo: ")    
                    if nisss in empleados["numeroISSS"]:
                        repetido=True
                    else:
                        repetido=False
                        empleados["numeroISSS"].append(nisss)
            else:
                empleados["numeroISSS"].append(nisss)
#Numero AFP---------------------------------------------------------------------------------
        nafp=input("Ingrese numero de AFP: ")
        while not (nafp.isnumeric() and len(nafp)==6):
            nafp=input("Ingrese el numero de AFP sin letras y de 6 digitos: ")
        if len(empleados["numeroafp"])==0:
            empleados["numeroafp"].append(nafp)
        elif len(empleados["numeroafp"])!=0:
            if nafp in empleados["numeroafp"]:
                repetido=True
                while repetido:
                    nafp=input("numero de AFP repetido. Ingrese uno nuevo: ")
                    while not (nafp.isnumeric() and len(nafp)==6):
                        nafp=input("Digite solo numeros y que contenga 6 digitos. Ingrese uno nuevo: ")    
                    if nafp in empleados["numeroafp"]:
                        repetido=True
                    else:
                        repetido=False
                        empleados["numeroafp"].append(nafp)
            else:
                empleados["numeroafp"].append(nafp)    
#Calculo de SAR, Descuento de ISSS, AFP y sueldo neto --------------------------------------------
        empleados["SAR"].append(sueldo)
        isss=round(sueldo*0.07)
        empleados["isss"].append(isss)
        afp=round(sueldo*0.0725)
        empleados["afp"].append(afp)
        sueldoneto=sueldo-renta-isss-afp
        empleados["sueldoneto"].append(sueldoneto)
#------------------------------------------------------------------------------------------------------------------------------------
#Inicio de la opcion B. Reescribir los datos del diccionario
#----------------------------------------------------------------------------------------------------------
#Diccionario vacio
    elif opcion==2:
        if len(empleados["codigoempleados"])==0:
            print("No hay registros. Ingrese datos y luego podra modificarlos")
#Diccionario con valores
#-----------------------------------------------------------------------------------------------------------
        elif len(empleados["codigoempleados"])!=0:
#Validamos que el codigo de empleado existe
#--------------------------------------------------------------------------------------------------            
            cempleado=input("Ingrese el codigo del empleado que desea modificar: ")
            
            while not (cempleado.isnumeric() and len(cempleado)==6):
                cempleado=input("Ingreso mal el codigo. Los codigos son numericos y de 6 digitos. Ingreselo nuevamente: ")
            
            if cempleado in empleados["codigoempleados"]:
                print("Codigo encontrado")
                seguir=True
                while seguir:
                    print("Digite el proceso que desea realizar")
                    print("1)MODIFICAR CODIGO")
                    print("2)MODIFICAR NOMBRE")
                    print("3)MODIFICAR SUELDO")
                    print("4)MODIFICAR ISSS")
                    print("5)MODIFICAR AFP")
                    print("6)ELIMINAR EMPLEADO")
                    print("7)CANCELAR MODIFICACION")
#---------------------------------------------------------------
#Validando la opcion
                    testopcion=True
                    op=input("Digite la opcion que desea realizar: ")
                    while testopcion:
                        try:
                            op=int(op)
                            testopcion=False
                        except:
                            op=input("No se admiten letras. Entre el digito de la opcion que desea realizar: ")
#-------------------------------------------------------------------------------------------------------                            
#Modificar codigo empleados
                    if op==1:
                        nuevocodigo=input("Ingrese el nuevo codigo del empleado: ")
                        while not (nuevocodigo.isnumeric() and len(nuevocodigo)==6 and nuevocodigo not in empleados["codigoempleados"]):
                            nuevocodigo=input("El nuevo codigo tiene que ser numerico, de 6 digitos y no tiene que repetirse. Ingreselo nuevamente: ")
                        for i in range(len(empleados["codigoempleados"])):
                            if cempleado==empleados["codigoempleados"][i]:
                                empleados["codigoempleados"][i]=nuevocodigo
                        print("El codigo ha sido modificado.")
                        seguir=False
                        input()
#----------------------------------------------------------------------------------------------------------------
#Modificar nombre
                    elif op==2:
                        nname=input("Ingrese el nuevo nombre completo del empleado: ").lstrip()
                        if any(chr.isdigit() for chr in nname)==True:
                            nombreincorrecto=True
                            while nombreincorrecto:
                                nname=input("El nombre ingresado contiene numeros. Ingresalo de nuevo: ").lstrip()
                                if any(chr.isdigit() for chr in nname)==True:
                                    nombreincorrecto=True
                                else:
                                    for i in range(len(empleados["codigoempleados"])):
                                        if cempleado==empleados["codigoempleados"][i]:
                                            empleados["nombreempleados"][i]=nname
                                    print("El nombre ha sido modificado.")
                                    nombreincorrecto=False
                        else:
                            for i in range(len(empleados["codigoempleados"])):
                                if cempleado==empleados["codigoempleados"][i]:
                                    empleados["nombreempleados"][i]=nname
                            print("El nombre ha sido modificado. ")
                            nombreincorrecto=False
            
                        seguir=False
                        input()
#-------------------------------------------------------------------------------------------------------------------
#Modificar Sueldo
                    
                    elif op==3:
                        testsueldo=True
                        nsueldo=input("Nuevo Sueldo mensual del empleado: $")
                        while testsueldo:
                            try:
                                nsueldo=float(nsueldo)
                                testsueldo=False
                                
                            except:
                                nsueldo=input("Ingrese solo numeros para el nuevo sueldo mensual del empleado: $")
                                
                        
                        for i in range(len(empleados["codigoempleados"])):
                            if cempleado==empleados["codigoempleados"][i]:
                                empleados["sueldomensual"][i]=nsueldo
                                if nsueldo<=500:
                                    nrenta=0
                                    empleados["renta"][i]=nrenta
                                elif nsueldo>500 and nsueldo<=1000:
                                    nrenta=round(nsueldo*0.10)
                                    empleados["renta"][i]=nrenta
                                elif nsueldo>1000:
                                    nrenta=round(nsueldo*0.20)
                                    empleados["renta"][i]=nrenta
                                    
                                empleados["SAR"][i]=nsueldo
                                nisss=round(nsueldo*0.07)
                                empleados["isss"][i]=nisss
                                nafp=round(nsueldo*0.0725)
                                empleados["afp"][i]=nafp
                                nsueldoneto=nsueldo-nrenta-nisss-nafp
                                empleados["sueldoneto"][i]=round(nsueldoneto)
                        print("Sueldo modificado.")
                        seguir=False
                        input()                  
#-------------------------------------------------------------------------------------------------------------------
#MODIFICAR ISSS
                    elif op==4:
                        nuevoISSS=input("Ingrese el nuevo ISSS del empleado: ")
                        while not (nuevoISSS.isnumeric() and len(nuevoISSS)==6):
                            nuevoISSS=input("Solo se aceptan numeros y un numero de 6 digitos: ")
                        
                        if nuevoISSS in empleados["numeroISSS"]:    
                            contisss=True
                            print("Este numero ya existe.")
                            while contisss:
                                nuevoISSS=input("Ingrese el nuevo numero ISSS del empleado: ")
                                while not (nuevoISSS.isnumeric() and len(nuevoISSS)==6):
                                    nuevoISSS=input("Solo se aceptan numeros y un numero de 6 digitos: ")
                                if nuevoISSS in empleados["numeroISSS"]:    
                                    print("Codigo repetido. Intentelo de nuevo")
                                    contisss=True
                                else:
                                    for i in range(len(empleados["codigoempleados"])):
                                        if cempleado==empleados["codigoempleados"][i]:
                                            empleados["numeroISSS"][i]=nuevoISSS
                                            contisss=False
                                            
                        elif nuevoISSS not in empleados["numeroISSS"]:
                            for i in range(len(empleados["codigoempleados"])):
                                if cempleado==empleados["codigoempleados"][i]:
                                    empleados["numeroISSS"][i]=nuevoISSS
                        
                        print("El ISSS ha sido modificado. ")
                        seguir=False
                        input()
#-------------------------------------------------------------------------------------------------------------------
#MODIFICAR AFP
                    elif op==5:
                        nuevoAFP=input("Ingrese el nuevo AFP del empleado: ")
                        while not (nuevoAFP.isnumeric() and len(nuevoAFP)==6):
                            nuevoAFP=input("Solo se aceptan numeros y un numero de 6 digitos: ")    
                        
                        if nuevoAFP in empleados["numeroafp"]:    
                            contafp=True
                            print("Este numero ya existe.")
                            while contafp:
                                nuevoAFP=input("Ingrese el nuevo AFP del empleado: ")
                                while not (nuevoAFP.isnumeric() and len(nuevoAFP)==6):
                                    nuevoAFP=input("Solo se aceptan numeros y un numero de 6 digitos: ")
                                if nuevoAFP in empleados["numeroafp"]:    
                                    print("Codigo repetido. Intentelo de nuevo")
                                    contafp=True
                                else:
                                    for i in range(len(empleados["codigoempleados"])):
                                        if cempleado==empleados["codigoempleados"][i]:
                                            empleados["numeroafp"][i]=nuevoAFP
                                            contafp=False        
                        
                        elif nuevoAFP not in empleados["numeroafp"]:
                            for i in range(len(empleados["codigoempleados"])):
                                if cempleado==empleados["codigoempleados"][i]:
                                    empleados["numeroafp"][i]=nuevoAFP
                        
                        print("El AFP ha sido modificado.")
                        seguir=False
                        input()
#--------------------------------------------------------------------------------------------------------------------
#ELIMINAR EMPLEADO
                    elif op==6:
                        for x in range (len(empleados["codigoempleados"])-1,-1,-1):
                            if cempleado==empleados["codigoempleados"][x]:
                                empleados["codigoempleados"].pop(x)
                                empleados["nombreempleados"].pop(x)
                                empleados["sueldomensual"].pop(x)
                                empleados["numeroISSS"].pop(x)
                                empleados["numeroafp"].pop(x)
                                empleados["SAR"].pop(x)
                                empleados["renta"].pop(x)
                                empleados["isss"].pop(x)
                                empleados["afp"].pop(x)
                                empleados["sueldoneto"].pop(x)
                        
                        print("Empleado eliminado")
                        seguir=False
                        input()
#--------------------------------------------------------------------------------------------------------------------
#Salir del menu de modificar
                    elif op==7:
                        print("Modificacion cancelada.")
                        seguir=False
                                
            else:
                print("Codigo no encontrado. Intentelo de nuevo")
                
        input()
#-------------------------------------------------------------------------------------------------------------
#Inicio de la opcion c. Generar reporte de planilla
    elif opcion==3:
        print("**********************Los necesitados**********************************************")
        print("Codigo| NOMBRES    | SUELDO MENSUAl| N° ISS| N° AFP| SAR  | RENTA| DESCUENTO ISS| DESCUENTO AFP| SALARIO NETO ")
        for x in range (len(empleados["codigoempleados"])):
            print(empleados["codigoempleados"][x],"",empleados["nombreempleados"][x],"      ",empleados["sueldomensual"][x],"        ",empleados["numeroISSS"][x],"",empleados["numeroafp"][x],"",empleados["SAR"][x]," ",empleados["renta"][x],"    ",empleados["isss"][x],"          ",empleados["afp"][x],"            ",empleados["sueldoneto"][x])
        input()
#Inicio de la opcion d. Terminar el programa
    elif opcion==4:
        continuar=False
        input("Programa terminado")
        print("**********************Los necesitados**********************************************")
#Cuando el usuario ingresa una opcion invalida
    else:
        print("Opcion invalida")
        input()