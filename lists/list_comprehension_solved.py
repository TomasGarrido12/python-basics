from functools import reduce 

# Ejercicios de List Comprehension

## Escribamos una funcion que filtre productos cuyo precio (price) sea mayor a n
def by_price_gt(n):
    return lambda price: price > n

def filter_products(products, cb):
    return [p for p in products if cb(p['price'])]

## Una funcion que devuelva el precio del total de productos
def total_price(products):
    return reduce(lambda x, y: x + y, [p['price'] for p in products], 0)

## Una funcion que devuelva el precio promedio de productos
def average_price(products):
    return total_price(products) / len(products)
