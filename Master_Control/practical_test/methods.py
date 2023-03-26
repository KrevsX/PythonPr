#  Copyright (c) 2023. By.Kevin Alas
#  All rights reserved
#  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia
#  accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget
#  metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from conection_parameters import collection


def create_movie(json_movies):
    insert = collection.insert_one(json_movies)
    print("Datos Ingresados Correctamente")
    print(insert.inserted_id)


def update_movie(_id, json_movies_update):
    query = {"_id": _id}
    new_values = {"$set": json_movies_update}
    show = {"_id": _id}
    docselected = collection.find(show)
    for show_json in docselected:
        print(show_json)
    updates = collection.update_one(query, new_values)
    print("Datos Actualizados Correctamente")
    print(updates.modified_count)


def delete_movie(_id):
    query = {"_id": _id}
    delete = collection.delete_one(query)
    print("Datos Eliminados Correctamente")
    print(delete.deleted_count)


def search_movies():
    search = collection.find()
    for searching in search:
        print(searching)


def search_movies_gte_date(year):
    query = {"fecha_publicacion.anio": {"$gte": year}}
    search = collection.find(query)
    for searching in search:
        print(searching)


def search_movies_lte_date(year):
    query = {"fecha_publicacion.anio": {"$lte": year}}
    selected = collection.find(query)
    for document in selected:
        print(document)


def search_movies_custom(field, value):
    query = {field: value}
    search = collection.find(query)
    for document in search:
        print(document)
