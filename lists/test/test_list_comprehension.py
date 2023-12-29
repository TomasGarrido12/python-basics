import unittest

# from list_comprehension_solved import filter_products, by_price_gt, total_price, average_price
from lists.list_comprehension_solved import filter_products, by_price_gt, total_price, average_price

def make_products():
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
    return products

products = make_products()

class TestListComprehensions(unittest.TestCase):

    def test_filter_products_price_bigger_than(self):
        self.assertEqual(filter_products(products, by_price_gt(100)), [
            { id: "7", "name": "VR Headset", "description": "Immersive virtual reality experience", "price": 105 },
            { id: "9", "name": "Fitness Tracker", "description": "Monitors health and activity metrics", "price": 300 },
            { id: "10", "name": "Digital Camera", "description": "High-resolution photos with easy connectivity", "price": 120 }
        ])

    def test_total_price(self):
        self.assertEqual(total_price(products), 1010)

    def test_average_price(self):
        self.assertEqual(average_price(products), 101)
