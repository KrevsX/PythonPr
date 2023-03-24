#  Copyright (c) 2023. By.Kevin Alas
#  All rights reserved
#  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia
#  accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget
#  metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["pruba_db"]

person = {
    "nombre": "Kevin",
    "Apellidos": "Winkler",
    "edad": 25,
    "email": "winkler@gmail.com",
    "direccion": {
        "calle": "av. 1574 St",
        "numero": "2166",
        "ciudad": "Arizona"
    }
}
# Guardar el Documento.....
personas = db["personas"]
personas.insert_one(person)
