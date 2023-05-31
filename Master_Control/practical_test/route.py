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
import json

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["Parcial"]
collection = db["peliculas"]
with open('peliculas.json') as file:
     data = json.load(file)
collection.insert_many(data)
print(collection.count_documents({}))

