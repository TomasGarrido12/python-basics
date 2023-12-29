# Listas y Lists comprehensions (ni idea como se traduce)

# Las listas en python son similares al concepto de ArrayList en C#, básicamente arrays
# que pueden almacenar una cantidad dinámica de elementos, o dicho de otra forma, crecer.

# Docu oficial: https://docs.python.org/es/3.12/tutorial/introduction.html#lists

# Algo muy interesante de Python es que su filosofía se basa en la simplicidad, y se refleja en las
# operaciones que podemos aplicar en las listas.

# Para meternos en tema vamos a usar una lista de productos (por ahora cada producto es un diccionario
# o dict hasta que veamos OOP https://docs.python.org/es/3/tutorial/datastructures.html#dictionaries)

products = [
    {id: "1", "name": "Wireless Earbuds", "description": "High-quality sound with noise cancellation feature", "price": 30 },
    {id: "2", "name": "Smartwatch", "description": "Fitness tracking and smartphone notifications", "price": 77 },
    {id: "3", "name": "Portable Charger", "description": "Fast-charging with long battery life", "price": 85 }
]

# Obtener un elemento por el indice
print(f"Primer producto de la lista: {products[0]['name']}")

# Obtener un elemento con indices negativos 🤯
print(f"Primer producto de la lista: {products[-1]['name']}")

# Obtener un subconjunto de la lista (slicing)
print(f"Los primeros tres productos: {products[:2]}")
print(f"Productos desde el 2do al 3ro: {products[1:3]}")
print(f"Los últimos dos productos: {products[-2:]}")

# Modificar un elemento de la lista
products[0]['price'] = 35
print(f"Producto actualizado: {products[0]}")

# Añadir un nuevo elemento al final de la lista
new_product = {"id": "11", "name": "Wireless Headphones", "description": "Comfortable over-ear design with studio-quality sound", "price": 150}
products.append(new_product)
print(f"Producto añadido: {products[-1]}")

# Insertar un elemento en una posición específica
mid_range_product = {"id": "4", "name": "E-Book Reader", "description": "Lightweight and portable with a high-resolution screen", "price": 80}
products.insert(1, mid_range_product)
print(f"Producto insertado: {products[2]}")

# Eliminar un elemento por su posición
del products[3]
print(f"Producto eliminado en la posición 4")

# Eliminar un elemento por su valor (primer coincidencia)
products.remove({"id": "11", "name": "Wireless Headphones", "description": "Comfortable over-ear design with studio-quality sound", "price": 150})
print(f"Producto Wireless Headphones eliminado")

# Python tiene algo llamado "list comprehensions", esencialmente una forma concisa de crear listas.

# Por ejemplo, creamos una lista de los nombres de los productos

product_names = [product['name'] for product in products]
print(f"Nombres de productos: {product_names}")

# Crear una lista de productos cuyo precio sea mayor a 50
expensive_products = [product for product in products if product['price'] > 50]
print(f"Productos con precio mayor a 50: {expensive_products}")

# Crear una lista con los precios actualizados aplicando un descuento del 10%
discounted_prices = [product['price'] * 0.9 for product in products]
print(f"Precios con descuento: {discounted_prices}")
