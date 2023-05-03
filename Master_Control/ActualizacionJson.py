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

# selecionar base de datos y la coleccion
db = client["mydatabase"]
collection = db["employees"]

collection.update_one({"first_name": "Nancy"}, {"$set": {"first_name": "KEVIN VAN WINKLE"}})


# este codigo solamente es para poder
# comprobar si se ha echo el cambio...
# busqueda = collection.find()
# for document in busqueda:
#     print(document)
