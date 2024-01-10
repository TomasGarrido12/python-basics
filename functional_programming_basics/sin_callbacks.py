# Esta función filtra y retorna una lista de productos cuyos precios están
# dentro del rango especificado por min_price y max_price.
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

#def filter_by_price_range(products, min_price, max_price):
    #return [p for p in products if p['price']>= min_price and p['price'] <= max_price]


#new_list = filter_by_price_range(products, 35, 50)


# Esta función filtra y retorna una lista de productos que contienen todos los
# 'keywords' dados tanto en el nombre como en la descripción del producto.
# Si keywords esta vacía devolver toda la lista.

def filter_by_keyword_in_title_and_description(products,keywords):
    return [p for p in products if keywords in p['name'] or keywords in p['description']]
    #if keywords is None:
        #return products
    #else:
       #new_list=[]
        #for dict in products:
            #products_values = dict.values()
            #for p in products_values:
                #if keywords in str(p):
                    #new_list.append(dict)
                #else:
                    #continue
        #return new_list    
    
    
new_list = filter_by_keyword_in_title_and_description(products, "")
print(new_list)

# Esta función identifica y retorna una lista de productos que tienen un stock
# por debajo del umbral especificado por stock_threshold.
def identify_low_stock_products(products, stock_threshold):
    return [p for p in products if p['stock']< stock_threshold]



new_list = identify_low_stock_products(products,20)
print(new_list)