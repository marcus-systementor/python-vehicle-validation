"""One possible validated version of the starter model."""


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False
        self.speed = 0
        self.fuel = 20
        self.max_fuel = 40

    def start(self):
        if self.is_running:
            return False
        self.is_running = True
        return True

    def stop(self):
        if not self.is_running:
            return False
        self.is_running = False
        return True

    def accelerate(self, amount):
        if not self.is_running:
            return False
        if amount <= 0:
            return False
        self.speed += amount
        return True

    def brake(self, amount):
        if amount <= 0:
            return False
        if self.speed == 0:
            return False
        if amount >= self.speed:
            self.speed = 0
        else:
            self.speed -= amount
        return True

    def refuel(self, amount):
        if amount <= 0:
            return False
        if self.fuel + amount > self.max_fuel:
            return False
        self.fuel += amount
        return True


class Car(Vehicle):
    pass
