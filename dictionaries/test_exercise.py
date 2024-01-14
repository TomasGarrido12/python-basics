import unittest

# from dictionaries.exercise_solved import group_by_category_and_average_price

from dictionaries.exercise import (
    group_by_category_and_average_price,
)


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


class TestDictionaries(unittest.TestCase):
    def test_group_by_category_and_average_price(self):
        self.assertEqual(
            group_by_category_and_average_price(products),
            {
                "Electronics": 72.5,
                "Accessories": 26.666666666666668,
                "Home": 0.0,
                "Fitness": 9.0,
            },
        )
