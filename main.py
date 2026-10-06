"""Show logical problems in a runnable vehicle program."""

from vehicle import Car


car = Car("Volvo", "V60")

print("Initial:", car.is_running, car.speed, car.fuel)
print("Stop before start:", car.stop())
print("Accelerate while stopped:", car.accelerate(50))
print("Brake too much:", car.brake(100))
print("Negative refuel:", car.refuel(-10))
print("Final:", car.is_running, car.speed, car.fuel)
