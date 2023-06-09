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

# from connection_parameters import *
# coneccion con el fin de llevar a cabo las consultas...
uri = "mongodb+srv://root:0000@cluster0.1jaakr4.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
db = client["KevinLemus"]
colecciones = db.list_collection_names()
if len(colecciones) > 0:
    print("Coleccion cargada............")
else:
    print("Error al cargar la Coleccion....")


# Probando que se extraen los archivos de MongoAtlas.....
# collection = db["customers"]
# for revCollection in collection.find():
#    print (revCollection)
def Ejercicio_1():
    query = db.orders.find({
        'details': {
            '$elemMatch': {
                'unit_price': {'$gt': 10}
            }
        }
    })
    print('todas las órdenes que incluyen al menos un detalle de un producto con un precio unitario mayor a $10.')
    for orden in query:
        print(orden)


def Ejercicio_2():
    from datetime import datetime
    # La fecha en variable para que se ejecute el query correctamente..
    fechaLimite = datetime(2006, 2, 1)

    query = db.orders.aggregate([
        {
            '$match': {
                'shipped_date': {'$lt': fechaLimite}
            }
        },
        {
            '$lookup': {
                'from': 'employees',
                'localField': 'employee_id',
                'foreignField': '_id',
                'as': 'employee'
            }
        },
        {
            '$unwind': '$employee'
        },
        {
            '$project': {
                'nombreCompleto': {'$concat': ['$employee.first_name', ' ', '$employee.last_name']},
                'numeroTelefonico': '$employee.business_phone'
            }
        }
    ])
    print(
        'Nombre completo y número telefónico de los empleados que han sido responsables de órdenes que se hayan '
        'enviado antes del 1 de febrero de 2006')
    for empleado in query:
        print(empleado)


def Ejercicio_3():
    query = db.orders.find({
        'customer_id': 27
    })
    print('Ordenes realizadas por el cliente con ID 27.')
    for orden in query:
        print(orden)


def Ejercicio_4():
    query = db.orders.aggregate([
        {
            '$match': {
                '_id': 30
            }
        },
        {
            '$unwind': '$details'
        },
        {
            '$lookup': {
                'from': 'products',
                'localField': 'details.product_id',
                'foreignField': '_id',
                'as': 'producto'
            }
        },
        {
            '$project': {
                'producto': {
                    '$arrayElemAt': ['$producto', 0]
                },
                'cantidad': '$details.quantity',
                'precio_unitario': '$details.unit_price',
                'descuento': '$details.discount'
            }
        }
    ])
    print('Detalles de los productos del pedido con ID 30.')
    for detalle in query:
        print(detalle)


def Ejercicio_5():
    query = db.orders.aggregate([
        {
            '$unwind': '$details'
        },
        {
            '$lookup': {
                'from': 'products',
                'localField': 'details.product_id',
                'foreignField': '_id',
                'as': 'producto'
            }
        },
        {
            '$project': {
                'nombre_producto': {'$arrayElemAt': ['$producto.product_name', 0]}
            }
        },
        {
            '$group': {
                '_id': None,
                'productos': {'$addToSet': '$nombre_producto'}
            }
        },
        {
            '$project': {
                '_id': 0,
                'productos': {'$map': {'input': '$productos', 'as': 'producto', 'in': {'nombreProducto': '$$producto'}}}
            }
        }
    ])
    print('Todos los nombres de los productos comprados.')
    for resultado in query:
        for producto in resultado['productos']:
            print(producto)


def Ejercicio_6():
    query = db.orders.aggregate([
        {
            '$lookup': {
                'from': 'customers',
                'localField': 'customer_id',
                'foreignField': '_id',
                'as': 'customer'
            }
        },
        {
            '$match': {
                'customer.company': 'Company A'
            }
        },
        {
            '$project': {
                'order_id': '$_id',
                'customer_company': {'$arrayElemAt': ['$customer.company', 0]},
                'order_date': 1,
                'shipped_date': 1,
                'shipping_fee': 1
            }
        }
    ])
    print('Todos los pedidos realizados por la empresa: “Company A”.')
    for pedidoCA in query:
        print(pedidoCA)
