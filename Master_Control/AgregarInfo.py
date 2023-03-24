from pymongo import MongoClient

# Creamos la coneccion a la base de Datos..
client = MongoClient('mongodb://localhost:27017')
# Obtener los datos de users desde la base de datos....
db = client['mydatabase']
# modelo de insercion......
# agreagar datos a un lugar en especifico
users = db['users']

user = {
    'name': 'winkle',
    'age': 28,
    'email': 'ejemploemail@gmail.com',
    'address': {
        "streer": "4151 Main St",
        "city": "San Francisco",
        "state": "CA",
        "zip": "94107"
    },
    "phone_numbers": [
        {
            "type": "home",
            "number": "555-555-5555"
        },
    ]
}

result = users.insert_one(user)
print(result.inserted_id)
print(result)
