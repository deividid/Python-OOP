class Glass:
    def __init__(self):
        self.content = 0

    capacity = 250

    def fill(self, value):
        if self.content + value <= Glass.capacity:
            self.content += value
            return f"Glass filled with {value} ml"

        else:
            return f"Cannot add {value} ml"

    def empty(self):
        self.content = 0
        return f"Glass is now empty"

    def info(self):
       return f"{Glass.capacity - self.content} ml left"

glass = Glass()

print(glass.fill(100))

print(glass.fill(200))

print(glass.empty())

print(glass.fill(200))

print(glass.info())
