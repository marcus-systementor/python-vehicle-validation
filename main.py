"""Show logical problems in a runnable vehicle program."""

from vehicle import Car


print("=== Test 1: Stoppa en redan stoppad bil ===")
stop_car = Car("Volvo", "V60")
print("Motor igång före:", stop_car.is_running)
print("Anrop: stop_car.stop()")
result = stop_car.stop()
print("Returnerar:", result)
print("Motor igång efteråt:", stop_car.is_running)
print()
print("Borde en operation som inte faktiskt ändrar något räknas som lyckad?")
print()

print("=== Test 2: Accelerera när bilen är stoppad ===")
accelerate_car = Car("Volvo", "V60")
print("Motor igång före:", accelerate_car.is_running)
print("Hastighet före:", accelerate_car.speed)
print("Anrop: accelerate_car.accelerate(50)")
result = accelerate_car.accelerate(50)
print("Returnerar:", result)
print("Motor igång efteråt:", accelerate_car.is_running)
print("Hastighet efteråt:", accelerate_car.speed)
print()
print("Borde bilen kunna accelerera när den är stoppad?")
print()

print("=== Test 3: Bromsa mer än aktuell hastighet ===")
brake_car = Car("Volvo", "V60")
brake_car.speed = 50
print("Hastighet före:", brake_car.speed)
print("Anrop: brake_car.brake(100)")
result = brake_car.brake(100)
print("Returnerar:", result)
print("Hastighet efteråt:", brake_car.speed)
print()
print("Borde hastigheten kunna bli negativ?")
print()

print("=== Test 4: Tanka med negativ mängd ===")
refuel_car = Car("Volvo", "V60")
refuel_car.fuel = 20
print("Bränsle före:", refuel_car.fuel)
print("Anrop: refuel_car.refuel(-10)")
result = refuel_car.refuel(-10)
print("Returnerar:", result)
print("Bränsle efteråt:", refuel_car.fuel)
print()
print("Borde en tankning kunna minska mängden bränsle?")
print()

print("\n\n===============================")
