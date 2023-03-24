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

db = client["mydatabase"]
# en caso de no existir la carpeta
# donde se almacenaran los datos
# la determianr un numbre se creara en mongo compas..

collection = db["mi_coleccion"]
document = {
    "nombre": "RIP VAN",
    "edad": 18,
    "ciudad": "Espania"
}

collection.insert_one(document)
# fomrato para
documentos = collection.find()
for documento in documentos:
    print(documento)
