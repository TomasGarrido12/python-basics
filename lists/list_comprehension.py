# Para una intro del tema ver el archivo lists/intro.py
# Sintaxis del List Comprehension newlist = [expression for item in iterable if condition == True]
# Sintaxis reduce() reduce(function, sequence[, initial])

from functools import reduce

products = [
    {id: "1", "name": "Wireless Earbuds", "description": "High-quality sound with noise cancellation feature", "price": 30 },
    {id: "2", "name": "Smartwatch", "description": "Fitness tracking and smartphone notifications", "price": 77 },
    {id: "3", "name": "Portable Charger", "description": "Fast-charging with long battery life", "price": 85 },
    {id: "4", "name": "Bluetooth Speaker", "description": "Compact size with clear, powerful sound", "price": 28 },
    {id: "5", "name": "Gaming Mouse", "description": "Ergonomic design with customizable buttons", "price": 72 },
    {id: "6", "name": "Waterproof Backpack", "description": "Durable and spacious with multiple compartments", "price": 100 },
    {id: "7", "name": "VR Headset", "description": "Immersive virtual reality experience", "price": 105 },
    {id: "8", "name": "Wireless Keyboard", "description": "Sleek design with long battery life", "price": 93 },
    {id: "9", "name": "Fitness Tracker", "description": "Monitors health and activity metrics", "price": 300 },
    {id: "10", "name": "Digital Camera", "description": "High-resolution photos with easy connectivity", "price": 120 }
]

# Desafíos

## Escribamos una funcion que filtre productos cuyo precio (price) sea mayor a n
def filter_products(lista_primer_desafio):
    return [x for x in lista_primer_desafio if x['price'] > 100]

productos_caros = filter_products(products)
print(productos_caros)

## Una funcion que devuelva el precio del total de productos
def total_price(valorA,valorB):
    return valorA + valorB

precio_total = reduce(total_price,[product['price'] for product in products])
print(f"El precio total de los productos es: ${precio_total}")

## Una funcion que devuelva el precio promedio de productos
def average_price(products):
    return print(f"El precio promedio de los productos es: ${precio_total/len(products)}")

average_price(products)






    #contador = 0  #me creo esta variable para tomarla como indice
    #for producto in lista_primer_desafio:
    #    print(f"Se esta analizando el siguiente producto y precio: {producto['name'], producto['price']}")
    #    if producto['price'] > 100:
    #        del lista_primer_desafio[contador]
    #        contador+=1
    #    else:
    #        contador+=1
    #return lista_primer_desafio