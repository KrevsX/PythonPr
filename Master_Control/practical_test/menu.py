#  Copyright (c) 2023. By.Kevin Alas
#  All rights reserved
#  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia
#  accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget
#  metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from functions import *
from methods import *

while True:
    print("MENU DE OPCIONES")
    print("1. CREAR BASE DE DATOS LOCAL: ")
    print("2. BUSCAR PELICULAS: ")
    print("3. AGREGAR NUEVA PELICULA: ")
    print("4. MODIFICAR DATOS DE PELICULAS: ")
    print("5. ELIMINAR PELICULA: ")
    print("6. SALIR: ")

    option = (input("PRESIONA EL NUMERO A SELECCIONAR/**"))
    if option == '1':
        from route import *
        from conection_parameters import *
        print("Hurray base de Datos Creada EXITOSAMENTE!!!...")
    elif option == '2':
        generate_search()
    elif option == '3':
        new_movie = create_json_movies()
        create_movie(new_movie)
    elif option == '4':
        id = int(input("INGRESAR ID DE LA PELICULA A MODIFICAR/..."))
        movie = create_json_updates()
        update_movie(id, movie)
    elif option == '5':
        id = int(input("INGRESAR ID DE LA PELICULA A ELIMINAR/...."))
        moviedeleted = delete_movie(id)
        delete_movie(moviedeleted)
    elif option == '6':
        print("BYE  BYEE  AMIX")
        break
    else:
        print("SELECCIONA UNA OPCION VALIDA/*****")


