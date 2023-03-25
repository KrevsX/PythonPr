#  Copyright (c) 2023. By.Kevin Alas
#  All rights reserved
#  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia
#  accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget
#  metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["Parcial"]


new_json = {
    "_id": 1,
    "clasificacion":"A",
    "titulo": "Rapidos y Furisos",
    "director": "Esteban Hernández Castelló",
    "distribuidor": "Universal Pictures",
    "tipo_pelicula": "Accion",
    "fecha_publicacion": {
    "dia": 11,
    "mes": "Marzo",
    "anio": 2009
    }
}

create_new_json = db["peliculas"]
create_new_json.insert_one(new_json)

