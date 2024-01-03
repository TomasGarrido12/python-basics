# Esta función general se utiliza para filtrar una lista de productos
# según un criterio definido en la función callback.
# - products: Lista de productos a filtrar.
# - callback: Función que define el criterio de filtrado.
def filter_by(products, callback):
    pass


# Esta función retorna un callback para filtrar productos por rango de precio.
# - min_price: Precio mínimo del rango.
# - max_price: Precio máximo del rango.
# La función retornada debe tomar un producto como argumento y devolver True
# si el precio del producto está dentro del rango especificado.
def is_in_price_range(min_price, max_price):
    pass


# Esta función retorna un callback para filtrar productos por palabras clave
# en el título y la descripción.
# - keywords: Lista de palabras clave a buscar.
# La función retornada debe tomar un producto como argumento y devolver True
# si todas las palabras clave están presentes tanto en el título como en
# la descripción del producto.
def contains_keywords(keywords):
    pass


# Esta función retorna un callback para identificar productos con bajo stock.
# - stock_threshold: Umbral de stock por debajo del cual se considera bajo stock.
# La función retornada debe tomar un producto como argumento y devolver True
# si la cantidad de stock del producto está por debajo del umbral especificado.
def is_below_stock_threshold(stock_threshold):
    pass


# Ejemplo de uso:
# products = [...]
# filtered_products = filter_by(products, is_in_price_range(10, 50))


# BONUS! 🌶️🌶️🌶️
# Combinando filtros

# Crear un filtrado flexible que permita aplicar múltiples criterios simultáneamente y que pueda adaptarse a futuras necesidades de filtrado.
# La firma de la función debería ser: filter_products(products, *callbacks)
# Una implementación posible podría ser una lista de callbacks, pero vamos a usar 'variable-length arguments', como para ver algo nuevo.

# Un ejemplo de como permitir una cantidad variable de argumentos es:


def my_function(someArg, *variableArgs):
    print(f"This is a simple arg {someArg}")
    for arg in variableArgs:
        print(arg)


my_function(1, 2, 3, "a", "b")

# Output:
# This is a simple arg 1
# 2
# 3
# a
# b


# Esta función debe aceptar una lista de productos y un número variable de funciones callback jeje
# Cada callback representa un criterio de filtrado diferente.
# Un producto debe cumplir con todos los criterios de los callbacks para ser incluido en la lista final.

# Ejemplo: `filtered_products = filter_products(products, filter_by_price_range(40, 80), identify_low_stock_products(30))`
