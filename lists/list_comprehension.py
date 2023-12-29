# Para una intro del tema ver el archivo lists/intro.py

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
#Tomo n como 100

#No se porque no filtra el producto que tiene un price de 120. En el FOR no llega hasta ese producto

lista_primer_desafio = products.copy()

def filter_products(lista_primer_desafio):
    contador = 0  #me creo esta variable para tomarla como indice
    for producto in lista_primer_desafio:
        print(f"Se esta analizando el siguiente producto y precio: {producto['name'], producto['price']}")
        if producto['price'] > 100:
            del lista_primer_desafio[contador]
            contador+=1
        else:
            contador+=1
    return lista_primer_desafio

productos_baratos = filter_products(lista_primer_desafio)

def cheap_products(productos_baratos):
    for producto in productos_baratos:
        print(f"Este producto tiene un valor igual o menor a 100: {producto['name'], producto['price']}")

cheap_products(productos_baratos)

## Una funcion que devuelva el precio del total de productos
lista_segundo_desafio = products.copy()

def total_price(lista_segundo_desafio):
    precio_total = 0
    for precio in lista_segundo_desafio:
        precio_total += precio['price']  
    return precio_total

precio_total = total_price(lista_segundo_desafio)
print(f"El precio acumulado es: ${precio_total} peronios")

## Una funcion que devuelva el precio promedio de productos
def average_price(precio_total):
    cantidad_elementos = len(lista_segundo_desafio)
    print(f"El precio promedio de los productos es: ${precio_total/cantidad_elementos} peronios")

average_price(precio_total)
