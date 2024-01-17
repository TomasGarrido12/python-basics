products = [
    {
        "id": "1",
        "name": "Wireless Earbuds",
        "description": "High-quality sound with noise cancellation feature",
        "price": 30,
        "category": "Electronics",
        "stock": 30,
    },
    {
        "id": "2",
        "name": "Bluetooth Speaker",
        "description": "Portable and waterproof speaker with deep bass",
        "price": 50,
        "category": "Electronics",
        "stock": 50,
    },
    {
        "id": "3",
        "name": "Smart Watch",
        "description": "Latest model with health and fitness tracking",
        "price": 200,
        "category": "Electronics",
        "stock": 200,
    },
    {
        "id": "4",
        "name": "Laptop Sleeve",
        "description": "Durable and water-resistant protection for your laptop",
        "price": 25,
        "category": "Accessories",
        "stock": 25,
    },
    {
        "id": "5",
        "name": "USB-C Hub",
        "description": "Expand your laptop's connectivity with multiple ports",
        "price": 40,
        "category": "Electronics",
        "stock": 40,
    },
    {
        "id": "6",
        "name": "Wireless Mouse",
        "description": "Ergonomic design with long battery life",
        "price": 20,
        "category": "Accessories",
        "stock": 20,
    },
    {
        "id": "7",
        "name": "LED Desk Lamp",
        "description": "Adjustable and energy-efficient desk light",
        "price": 35,
        "category": "Home",
        "stock": 35,
    },
    {
        "id": "8",
        "name": "Yoga Mat",
        "description": "Non-slip mat for yoga and exercise routines",
        "price": 15,
        "category": "Fitness",
        "stock": 15,
    },
    {
        "id": "9",
        "name": "Water Bottle",
        "description": "Insulated stainless steel bottle to keep drinks cold",
        "price": 18,
        "category": "Fitness",
        "stock": 18,
    },
    {
        "id": "10",
        "name": "Backpack",
        "description": "Spacious and comfortable for everyday use",
        "price": 60,
        "category": "Accessories",
        "stock": 60,
    },
]


# Esta función general se utiliza para filtrar una lista de productos
# según un criterio definido en la función callback.
# - products: Lista de productos a filtrar.
# - callback: Función que define el criterio de filtrado.
def filter_by(product, callback):
    return [p for p in product if callback(p)]


# Esta función retorna un callback para filtrar productos por rango de precio.
# - min_price: Precio mínimo del rango.
# - max_price: Precio máximo del rango.
# La función retornada debe tomar un producto como argumento y devolver True
# si el precio del producto está dentro del rango especificado.
def is_in_price_range(min_price, max_price):
    return (
        lambda product: True
        if product["price"] > min_price and product["price"] < max_price
        else False
    )


# Esta función retorna un callback para filtrar productos por palabras clave
# en el título y la descripción.
# - keywords: Lista de palabras clave a buscar.
# La función retornada debe tomar un producto como argumento y devolver True
# si todas las palabras clave están presentes tanto en el título como en
# la descripción del producto.
def contains_keywords(keywords):
    return (
        lambda product: True
        if keywords in product["name"] or keywords in product["description"]
        else False
    )

    # Esta solución solo aplica si la keywords es una sola palabra, es decir, no contempla una lista de keywords


# Esta función retorna un callback para identificar productos con bajo stock.
# - stock_threshold: Umbral de stock por debajo del cual se considera bajo stock.
# La función retornada debe tomar un producto como argumento y devolver True
# si la cantidad de stock del producto está por debajo del umbral especificado.
def is_below_stock_threshold(stock_threshold):
    return lambda product: True if product["stock"] < stock_threshold else False

    # Ejemplo de uso:
    # products = [...]
    filtered_products = filter_by(products, is_in_price_range(10, 50))

    filtered_products = filter_by(products, contains_keywords("Bluetooth"))

    filtered_products = filter_by(products, is_below_stock_threshold(35))


# BONUS! 🌶️🌶️🌶️
# Combinando filtros

# Crear un filtrado flexible que permita aplicar múltiples criterios simultáneamente y que pueda adaptarse a futuras necesidades de filtrado.
# La firma de la función debería ser: filter_products(products, *callbacks)
# Una implementación posible podría ser una lista de callbacks, pero vamos a usar 'variable-length arguments', como para ver algo nuevo.

# Un ejemplo de como permitir una cantidad variable de argumentos es:


# def my_function(someArg, *variableArgs):
#     raise


# my_function(1, 2, 3, "a", "b")

# Output:
# This is a simple arg 1
# 2
# 3
# a
# b


# Esta función debe aceptar una lista de productos y un número variable de funciones callback jeje
# Cada callback representa un criterio de filtrado diferente.
# Un producto debe cumplir con todos los criterios de los callbacks para ser incluido en la lista final.
def filter_products(products, *callbacks):
    filtrados = []

    for prod in products:
        matches_all_criteria = True
        for callback in callbacks:
            if not callback(prod):
                matches_all_criteria = False
                break
        if matches_all_criteria:
            filtrados.append(prod)

    return filtrados


def foo():
    print("foo!")


def bar():
    print("bar!")


lista = [foo, bar]

for fn in lista:
    print(fn())

# Ejemplo: `filtered_products = filter_products(products, filter_by_price_range(40, 80), identify_low_stock_products(30))`

# Higher order function (funciones que reciben funciones como parametro)
# Callbacks son funciones que son pasadas a otra funcion como parametro (callback)
# Funciones en python pueden ser tratadas como cualquier otro valor, podemos retornar una funcion dentro de otra funcion(first class citizen)


products2 = [
    {
        "id": "1",
        "name": "Wireless Earbuds",
        "description": "High-quality sound with noise cancellation feature",
        "price": 30,
        "category": "Electronics",
        "stock": 30,
    },
    {
        "id": "2",
        "name": "Bluetooth Speaker",
        "description": "Portable and waterproof speaker with deep bass",
        "price": 50,
        "category": "Electronics",
        "stock": 70,
    },
]


def identify_low_stock_products(stock):
    return lambda prod: prod["stock"] < stock


filtered_products = filter_products(
    products2, is_in_price_range(40, 80), identify_low_stock_products(60)
)

print(filtered_products)
