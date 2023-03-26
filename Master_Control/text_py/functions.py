#  Copyright (c) 2023. By.Kevin Alas
#  All rights reserved
#  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia
#  accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget
#  metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from methods import *


def create_json_movies():
    _id = int(input("ID: "))
    while not _id:
        print("No se permiten espacios vacios..")
        _id = int(input("ID: "))
    clasificacion = input("CLASIFICACION: ")
    while not clasificacion:
        print("No se permiten espacios vacios..")
        clasificacion = (input("CLASIFICACION: "))
    titulo = input("TITULO:")
    while not titulo:
        print("No se permiten espacios vacios..")
        titulo = input("TITULO:")
    director = input("DIRECTOR: ")
    while not director:
        print("No se permiten espacios vacios..")
        director = input("DIRECTOR: ")
    distribuidor = input("DISTRIBUIDOR: ")
    while not distribuidor:
        print("No se permiten espacios vacios..")
        distribuidor = input("DISTRIBUIDOR: ")
    genero_pelicula = input("GENERO DE PELICULA: ")
    while not genero_pelicula:
        print("No se permiten espacios vacios..")
        genero_pelicula = input("GENERO DE PELICULA: ")
    print("Fecha de Publicacion: ")
    dia = int(input("DIA: "))
    while not dia:
        print("No se permiten espacios vacios..")
        dia = int(input("DIA:"))
    mes = (input("MES: "))
    while not mes:
        print("No se permiten espacios vacios..")
        mes = (input("MES:"))
    anio = int(input("AÑO: "))
    while not anio:
        print("No se permiten espacios vacios..")
        anio = int(input("AÑO: "))

    new_book = {
        "_id": _id,
        "clasificacion": clasificacion,
        "titulo": titulo,
        "director": director,
        "distribuidor": distribuidor,
        "tipo_pelicula": genero_pelicula,
        "fecha_publicacion": {
            "dia": dia,
            "mes": mes,
            "anio": anio
        }
    }
    return new_book


def gerenate_search():

    print("OPCIONES DE BUSQUEDA: ")
    print("1. BUSQUEDA GLOBAL: ***")
    print("2. BUSQUEDA POR FECHA DE PUBLICACION: ***")
    print("3. BUSQUEDA PERSONALIZADA: ***")
    option = input("Ingrese una Opcion/-****")
    while option not in ['1', '2', '3']:
        print("INGRESA UNA OPCION VALIDA******")
        option = input("Ingrese una Opcion/-****")
    if option == '1':
        search_movies()
    elif option == '2':
        print("ACONTINUACION SELECIONA UNA OPCION ")
        print("1. Ver Publicaciones mayor segun año:")
        print("2. Ver Publicaciones Menor segun año:")
        toption = input("Opcion = ")
        while toption not in ['1','2']:
            print("INGRESA UNA OPCION VALIDA******")
            toption = input("Opcion = ")
        if toption == '1':
            ano = int(input("INGRESE UN AÑO: "))
            search_movies_gte_date(ano)
        elif toption == '2':
            ano = int(input("INGRESAR UN AÑO: "))
            search_movies_lte_date(ano)
        else:
            print("Ingrese un Valor Valido")


def create_json_updates():
    print("Menu de Opciones../")
    print("1. Modificar todo el modulo de informacion/....")
    print("2. Modificacion Personalizada/....")
    option = input("INGRESA UNA DE LAS OPCIONES/....")
    while option not in ['1', '2']:
        option = input("INGRESA UNA DE LAS OPCIONES/....")
    if option == '1':
        clasificacion = input("CLASIFICACION: ")
        while not clasificacion:
            print("No se permiten espacios vacios..")
            clasificacion = (input("CLASIFICACION: "))
        titulo = input("TITULO:")
        while not titulo:
            print("No se permiten espacios vacios..")
            titulo = input("TITULO:")
        director = input("DIRECTOR: ")
        while not director:
            print("No se permiten espacios vacios..")
            director = input("DIRECTOR: ")
        distribuidor = input("DISTRIBUIDOR: ")
        while not distribuidor:
            print("No se permiten espacios vacios..")
            distribuidor = input("DISTRIBUIDOR: ")
        genero_pelicula = input("GENERO DE PELICULA: ")
        while not genero_pelicula:
            print("No se permiten espacios vacios..")
            genero_pelicula = input("GENERO DE PELICULA: ")
        print("Fecha de Publicacion: ")
        dia = int(input("DIA: "))
        while not dia:
            print("No se permiten espacios vacios..")
            dia = int(input("DIA:"))
        mes = (input("MES: "))
        while not mes:
            print("No se permiten espacios vacios..")
            mes = (input("MES:"))
        anio = int(input("AÑO: "))
        while not anio:
            print("No se permiten espacios vacios..")
            anio = int(input("AÑO: "))

        new_book = {
            "clasificacion": clasificacion,
            "titulo": titulo,
            "director": director,
            "distribuidor": distribuidor,
            "tipo_pelicula": genero_pelicula,
            "fecha_publicacion": {
                "dia": dia,
                "mes": mes,
                "anio": anio
            }
        }
        return new_book
    elif option == '2':
        claves = "_id, clasificacion, titulo, director, distribuidor, tipo_pelicula, fecha_publicacion, dia, mes, anio"
        print("Los Indices a Utilizar son:")
        print(claves)
        indice = input("INGRESAR EL INDICE/....")
        valor = input("INGRESE EL VALOR A MODIFICAR/....")
        while not all([indice, valor]):
            print("SE NECESITA OBLIGATORAMENTE UN INDICE Y UN VALOR..")
            print("INDICES: \n", claves)
            indice = input("INGRESAR EL INDICE/....")
            valor = input("INGRESE EL VALOR A MODIFICAR/....")
        info_movies = {indice: valor}
        return info_movies
    else:
        print("LOS DATOS INGRESADOS SON INVALIDOS.....")
