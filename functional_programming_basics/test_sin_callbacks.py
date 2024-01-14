import unittest

# from functional_programming_basics.sin_callbacks import filter_by_price_range
from functional_programming_basics.sin_callbacks import (
    filter_by_price_range,
    filter_by_keyword_in_name_and_description,
    identify_low_stock_products,
)

# Otra lista, similar a la anterior pero con categorias
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


class TestCallbacks(unittest.TestCase):
    def test_filter_by_price_range(self):
        self.assertEqual(
            filter_by_price_range(products, 35, 50),
            [
                {
                    "id": "2",
                    "name": "Bluetooth Speaker",
                    "description": "Portable and waterproof speaker with deep bass",
                    "price": 50,
                    "category": "Electronics",
                    "stock": 50,
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
                    "id": "7",
                    "name": "LED Desk Lamp",
                    "description": "Adjustable and energy-efficient desk light",
                    "price": 35,
                    "category": "Home",
                    "stock": 35,
                },
            ],
        )

    def test_filter_by_keyword_in_name_and_description_yoga(self):
        self.assertEqual(
            filter_by_keyword_in_name_and_description(products, ["Yoga"]),
            [
                {
                    "id": "8",
                    "name": "Yoga Mat",
                    "description": "Non-slip mat for yoga and exercise routines",
                    "price": 15,
                    "category": "Fitness",
                    "stock": 15,
                }
            ],
        )

    #def test_filter_by_keyword_in_name_and_description_empty(self):
        self.assertEqual(
            filter_by_keyword_in_name_and_description(products, [""]), products
        )

    #def test_identify_low_stock_products(self):
        expected_result = [
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
        ]
        self.assertEqual(identify_low_stock_products(products, 20), expected_result)
