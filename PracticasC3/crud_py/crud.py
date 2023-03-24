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
import json

def read_employees(id=None):
    if id is not None:
        query ={"_id": id}
        document = collection.find_one(query)
        print(document)
    else:
        document = collection.find()
        for documents in document:
            print(documents)

def create_employee(json_employees):
    result = collection.insert_one(json_employees)
    print(result.inserted_id)

def update_employee(id, json_employee_update):
    query = {"_id": id}
    new_values = {"$set": json_employee_update}
    result = collection.update_one(query, new_values)
    print(result.modified_count)


def search_employees():
    document = collection.find()
    for documents in document:
        print(documents)

def delete_employee(id):
    query = {"_id": id}
    result = collection.delete_one(query)
    print(result.deleted_count)