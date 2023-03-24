#  Copyright (c) 2023. By.Kevin Alas
#  All rights reserved
#  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia
#  accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget
#  metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

def create_json_employee():
    _id = int(input("ID: "))
    while not _id:
        print("NO SE PERMITEN ESPACIOS EN BLANCO")
        _id = input("ID: ")
    company = input("Company: ")
    while not company:
        print("NO SE PERMITEN ESPACIOS EN BLANCO")
        company = input("Company: ")
    last_name = input("Last Name: ")
    while not last_name:
        print("NO SE PERMITEN ESPACIOS EN BLANCO")
        last_name = input("Last Name: ")
    first_name = input("First Name: ")
    while not first_name:
        print("NO SE PERMITEN ESPACIOS EN BLANCO")
        first_name = input("First Name: ")
    email = input("Email: ")
    while not email:
        print("NO SE PERMITEN ESPACIOS EN BLANCO")
        email = input("Email: ")
    job_title = input("Job Title: ")
    while not job_title:
        print("NO SE PERMITEN ESPACIOS EN BLANCO")
        job_title= input("Job Title: ")
    business_phone = input("Business Phone: ")
    while not business_phone:
        print("NO SE PERMITEN ESPACIOS EN BLANCO")
        business_phone = input("Business Phone: ")
    address = input("Address: ")
    while not address:
        print("NO SE PERMITEN ESPACIOS EN BLANCO")
        address = input("Address: ")

    employee = {
        "_id": _id,
        "company": company,
        "last_name": last_name,
        "first_name": first_name,
        "email": email,
        "job_title": job_title,
        "business_phone": business_phone,
        "address": address
    }
    return employee

def create_json_update():
    print ("Menu de Opciones...")
    print("1. Modificar todos los datos del documento/...")
    print("2. Modificar un elemento del documento/..")
    opcion = input("Ingresa una opcion/..")
    while opcion not in['1', '2']:
        opcion = input("Ingresa una de las opcion Validas...")
    if opcion =="1":
        company = input("Company: ")
        while not company:
            print("NO SE PERMITEN ESPACIOS EN BLANCO")
            company = input("Company: ")
        last_name = input("Last Name: ")
        while not last_name:
            print("NO SE PERMITEN ESPACIOS EN BLANCO")
            last_name = input("Last Name: ")
        first_name = input("First Name: ")
        while not first_name:
            print("NO SE PERMITEN ESPACIOS EN BLANCO")
            first_name = input("First Name: ")
        email = input("Email: ")
        while not email:
            print("NO SE PERMITEN ESPACIOS EN BLANCO")
            email = input("Email: ")
        job_title = input("Job Title: ")
        while not job_title:
            print("NO SE PERMITEN ESPACIOS EN BLANCO")
            job_title = input("Job Title: ")
        business_phone = input("Business Phone: ")
        while not business_phone:
            print("NO SE PERMITEN ESPACIOS EN BLANCO")
            business_phone = input("Business Phone: ")
        address = input("Address: ")
        while not address:
            print("NO SE PERMITEN ESPACIOS EN BLANCO")
            address = input("Address: ")

        employee = {
            "company": company,
            "last_name": last_name,
            "first_name": first_name,
            "email": email,
            "job_title": job_title,
            "business_phone": business_phone,
            "address": address
        }
        return employee
    elif opcion =="2":
        indice = input("Ingresar el indice/...")
        valor = input("Ingrese el valor a modificar/...")
        while not all([indice, valor]):
            print("SE NECESITA LA CLAVE: Y EL VALOR: //..")
            indice = input("Ingresar el indice/...")
            valor = input("Ingrese el valor a modificar/...")
        employee = {indice:valor}
        return employee
    else:
        print ("LOS DATOS INGRESADOS NO SON VALIDOS...")