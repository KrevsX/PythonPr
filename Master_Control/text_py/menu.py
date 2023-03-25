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
    print("1. BUSCAR LIBRO: ")
    print("2. AGREGAR NUEVO LIBRO: ")
    print("3. MODIFICAR DATOS DE LIBROS: ")
    print("4. ELIMINAR LIBRO: ")
    print("5. AGREGAR NUEVO LIBRO: ")
    option = int(input("PRESIONA EL NUMERO A SELECCIONAR/**"))
    if option == 2:
        new_movie = create_json_movies()
        create_movie(new_movie)
