from functools import reduce
import itertools

products = [
    {
        "id": "1",
        "name": "Wireless Earbuds",
        "description": "High-quality sound with noise cancellation feature",
        "price": 30,
        "category": "Electronics",
    },
    {
        "id": "2",
        "name": "Bluetooth Speaker",
        "description": "Portable and waterproof speaker with deep bass",
        "price": 50,
        "category": "Electronics",
    },
    {
        "id": "3",
        "name": "Smart Watch",
        "description": "Latest model with health and fitness tracking",
        "price": 200,
        "category": "Electronics",
    },
    {
        "id": "4",
        "name": "Laptop Sleeve",
        "description": "Durable and water-resistant protection for your laptop",
        "price": 25,
        "category": "Accessories",
    },
    {
        "id": "5",
        "name": "USB-C Hub",
        "description": "Expand your laptop's connectivity with multiple ports",
        "price": 40,
        "category": "Electronics",
    },
    {
        "id": "6",
        "name": "Wireless Mouse",
        "description": "Ergonomic design with long battery life",
        "price": 20,
        "category": "Accessories",
    },
    {
        "id": "7",
        "name": "LED Desk Lamp",
        "description": "Adjustable and energy-efficient desk light",
        "price": 35,
        "category": "Home",
    },
    {
        "id": "8",
        "name": "Yoga Mat",
        "description": "Non-slip mat for yoga and exercise routines",
        "price": 15,
        "category": "Fitness",
    },
    {
        "id": "9",
        "name": "Water Bottle",
        "description": "Insulated stainless steel bottle to keep drinks cold",
        "price": 18,
        "category": "Fitness",
    },
    {
        "id": "10",
        "name": "Backpack",
        "description": "Spacious and comfortable for everyday use",
        "price": 60,
        "category": "Accessories",
    },
]
# Lectura recomendada
# https://ellibrodepython.com/diccionarios-en-python

# Principal ventaja de un diccionario (HashMap)
# - Acceso, inserción y borrado rápido de elementos

# Desventaja
# - No garantizan un orden de las keys
# - Usan mucha memoria
# - Dependientes de la función de hashing
#
# Sobre hashing:
# - https://es.wikipedia.org/wiki/Funci%C3%B3n_hash#Uniforme
# - https://www.interviewcake.com/concept/java/hash-map


# El resultado deberia ser un diccionario -> { 'categoria_x': 10, 'categoria_y': 20, etc }
# Agrupar por categoria y sacar el promedio del precio de cada categoria
def group_by_category_and_average_price(products):
    grupos = {}
    def key_func(k):
        return k['category']
    
    
    for key, value in itertools.groupby(sorted(products, key=key_func), key_func):
        variable_a = key
        variable_b = (list(value))
        #grupos = grupos.append(variable_b)
        print(variable_a,variable_b)
    
    
    for p in products:
        print(p["category"])

    for category, group in itertools.groupby(products, key = lambda x: x["category"]):
        grupos[category] = list(group)

    return grupos

dictionario = group_by_category_and_average_price(products)

print(dictionario)
    
    

    
