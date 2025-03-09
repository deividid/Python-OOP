class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = True

    def install(self, app, momory_needed):
        if self.is_on == True and self.memory >= momory_needed:
            self.apps.append(app)
            self.memory -= momory_needed
            return f"Installing {app}"

        elif self.is_on == False and self.memory >= momory_needed:
            return f"Turn on your phone to install {app}"

        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"

smartphone = Smartphone(100)

print(smartphone.install("Facebook", 60))

smartphone.power()

print(smartphone.install("Facebook", 60))

print(smartphone.install("Messenger", 20))

print(smartphone.install("Instagram", 40))

print(smartphone.status())