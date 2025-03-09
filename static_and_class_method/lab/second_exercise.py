class Shop:



    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}
        self.count = 0

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def add_item(self, name):
        if len(self.items.keys()) < self.capacity - self.count:
            if name in self.items.keys():
                self.items[name] += 1
                self.count += 1

            else:
                self.items[name] = 1

            return f"{name} added to the shop"

        else:
            return "Not enough capacity in the shop"


    def remove_item(self, name, amount):
        if name in self.items.keys() and self.items[name] >= amount:
            if self.items[name] == amount:
                self.items.pop(name)

            else:
                slef.items[name] -= amount

            return f"{amount} {name} removed from the shop"

        else:
            return f"Cannot remove {amount} {name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)

small_shop = Shop.small_shop("Fashion Boutique", "Clothes")

print(fresh_shop)

print(small_shop)
print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))
print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)