from shop.project.product import Product
from shop.project.product_repository import ProductRepository
from shop.project.food import Food
from shop.project.drink import Drink

food = Food("apple")

drink = Drink("water")

repo = ProductRepository()

repo.add(food)

repo.add(drink)

print(repo.products)

print(repo.find("water"))

repo.find("apple").decrease(5)

print(repo)