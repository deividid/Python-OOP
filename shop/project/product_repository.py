from typing import List

from project.product import Product


class ProductRepository(Product):

    def __init__(self):
        self.products: List[Product] = []

    def add(self, p: Product):
        self.products.append(p)

    def find(self, product_name):
        for p in self.products:
            if p.name == product_name:
                return p

    def remove(self, product_name):
        for p in self.products:
            if p.name == product_name:
                self.products.remove(p)

    def __repr__(self):
        result = ""
        for p in self.products:
            result += f"{p.name}: {p.quantity}\n"

        return result[:-1]



