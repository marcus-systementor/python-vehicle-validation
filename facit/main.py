"""Manual scenarios for the validated vehicle model."""

from vehicle import Car


car = Car("Volvo", "V60")

print("Initial:", car.is_running, car.speed, car.fuel)
print("Stop before start:", car.stop())
print("Accelerate while stopped:", car.accelerate(50))
print("Brake too much:", car.brake(100))
print("Negative refuel:", car.refuel(-10))
print("Final:", car.is_running, car.speed, car.fuel)

print("Start:", car.start())
print("Start again:", car.start())
print("Accelerate 20:", car.accelerate(20))
print("Accelerate -5:", car.accelerate(-5))
print("Brake 50:", car.brake(50))
print("Refuel 30:", car.refuel(30))
print("Refuel 10:", car.refuel(10))
print("Stop:", car.stop())
print("Stop again:", car.stop())
print("Final checks:", car.is_running, car.speed, car.fuel)
