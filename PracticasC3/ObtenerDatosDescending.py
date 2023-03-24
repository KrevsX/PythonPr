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

# CONSULTA DE DOCUMENTOS DE UNA BASE DE DATOS
# Y UNA COLECCION
db = client["mydatabase"]
coleccion = db["users"]  # buscar informacion de la coleccion

# obtener datos segun clave en orden descendiente
# DESCENDIN = DESCENDIENTE
# ASCENDIND = ASCENDIENTE
orden = [("age", pymongo.ASCENDING)]
documentOrder = coleccion.find().sort(orden)
for document in documentOrder:
    print(document)
