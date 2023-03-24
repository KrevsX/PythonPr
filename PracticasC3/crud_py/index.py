#  Copyright (c) 2023. By.Kevin Alas
#  All rights reserved
#  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia
#  accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget
#  metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

from crud import *
from ba_functions import *

while True:
    print ("MENU DE OPCIONES")
    print("1. Ver todos los Registros")
    print("2. Buscar los Registros")
    print("3. Agregar un registro")
    print("4. Modificar un Registro")
    print("5. Eliminar un registro")
    print("6. Busqueda Global..")
    print("7. Salir del sistema")

    opcion = input("Ingrese una Opcion...")
    if opcion == "1":
        read_employees()
    elif opcion == "2":
        id= int(input("Ingrese el ID a buscar..."))
        read_employees(id)
    elif opcion == "3":
        employee = create_json_employee()
        create_employee(employee)
    elif opcion == "4":
        id= int(input("Ingrese el ID a modificar..."))
        employee = create_json_update()
        update_employee(id, employee)
    elif opcion == "5":
        id = int(input("Ingrese el ID a Eliminar..."))
        employee = delete_employee(id)
        delete_employee(employee)
    elif opcion == "6":
        search_employees()
    elif opcion =="7":
        break
    else:
        print("ERROR INGRESE UNA DE LAS OPCIONES VALIDAS//....")
