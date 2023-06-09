#  Copyright (c) 2023. By.Kevin Alas
#  All rights reserved
#  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia
#  accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget
#  metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.


while True:
    print('-----------------------------------------------------------------------------')
    print("MENU DE OPCIONES PARA VALIDAR CONEXION A MONGOATLAS Y PROBAR LAS CONSULTAS")
    print("1. COMPROBAR LA CONEXION A MONGO-ATLAS: ")
    print("2. EJERCICIO 1")
    print("3. EJERCICIO 2")
    print("4. EJERCICIO 3")
    print("5. EJERCICIO 4")
    print("6. EJERCICIO 5")
    print("7. EJERCICIO 6")
    print("8. SALIR: ")

    option = (input("PRESIONA EL NUMERO A SELECCIONAR/**"))
    if option == '1':
        from connection_parameters import*
    elif option == '2':
        from funciones import *
        Ejercicio_1()
    elif option == '3':
        from funciones import *
        Ejercicio_2()
    elif option == '4':
        from funciones import *
        Ejercicio_3()
    elif option == '5':
        from funciones import *
        Ejercicio_4()
    elif option == '6':
        from funciones import*
        Ejercicio_5()
    elif option == '7':
        from funciones import *
        Ejercicio_6()
    elif option == '8':
        print("BYEE-BYEE")
        break
    else:
        print("SELECCIONA UNA OPCION VALIDA/*****")