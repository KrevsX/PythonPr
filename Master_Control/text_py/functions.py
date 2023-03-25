#  Copyright (c) 2023. By.Kevin Alas
#  All rights reserved
#  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia
#  accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget
#  metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

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
    generoPelicula= input("GENERO DE PELICULA: ")
    while not generoPelicula:
        print("No se permiten espacios vacios..")
        generoPelicula = input("GENERO DE PELICULA: ")
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
        "tipo_pelicula": generoPelicula,
        "fecha_publicacion": {
            "dia": dia,
            "mes": mes,
            "anio": anio
        }
    }
    return new_book
