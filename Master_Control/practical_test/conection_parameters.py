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
collection = db["peliculas"]

if "peliculas" not in db.list_collection_names():
    print()
else:
    print("La colección ya existe en la base de datos.")
