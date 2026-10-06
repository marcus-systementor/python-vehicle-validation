"""A runnable vehicle model with intentionally missing validation."""


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False
        self.speed = 0
        self.fuel = 20
        self.max_fuel = 40

    def start(self):
        self.is_running = True
        return True

    def stop(self):
        self.is_running = False
        return True

    def accelerate(self, amount):
        self.speed += amount
        return True

    def brake(self, amount):
        self.speed -= amount
        return True

    def refuel(self, amount):
        self.fuel += amount
        return True


class Car(Vehicle):
    pass
