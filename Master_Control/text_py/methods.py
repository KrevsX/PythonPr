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

def update_movies(id, json_movies_update):
    query = {"_id": id}
    new_values = {"$set": json_movies_update}
    updates = collection.update_one(query, new_values)
    print("Datos Actualizados Correctamente")
    print(updates.inserted_id)


