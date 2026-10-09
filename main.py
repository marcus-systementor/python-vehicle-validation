"""Show logical problems in a runnable vehicle program."""

from vehicle import Car


car = Car("Volvo", "V60")

print("=== Startläge ===")
print("Motor igång:", car.is_running)
print("Hastighet:", car.speed)
print("Bränsle:", car.fuel, "/", car.max_fuel)
print()

print("=== Test 1: Stoppa en redan stoppad bil ===")
print("Anrop: car.stop()")
result = car.stop()
print("Returnerar:", result)
print("Motor igång efteråt:", car.is_running)
print()
print("Borde en operation som inte faktiskt ändrar något räknas som lyckad?")
print()

print("=== Test 2: Accelerera när bilen är stoppad ===")
print("Anrop: car.accelerate(50)")
result = car.accelerate(50)
print("Returnerar:", result)
print("Motor igång:", car.is_running)
print("Hastighet efteråt:", car.speed)
print()
print("Borde bilen kunna accelerera när den är stoppad?")
print()

print("=== Test 3: Bromsa mer än aktuell hastighet ===")
print("Hastighet före:", car.speed)
print("Anrop: car.brake(100)")
result = car.brake(100)
print("Returnerar:", result)
print("Hastighet efteråt:", car.speed)
print()
print("Borde hastigheten kunna bli negativ?")
print()

print("=== Test 4: Tanka med negativ mängd ===")
print("Bränsle före:", car.fuel)
print("Anrop: car.refuel(-10)")
result = car.refuel(-10)
print("Returnerar:", result)
print("Bränsle efteråt:", car.fuel)
print()
print("Borde en tankning kunna minska mängden bränsle?")
print()

print("=== Slutläge ===")
print("Motor igång:", car.is_running)
print("Hastighet:", car.speed)
print("Bränsle:", car.fuel, "/", car.max_fuel)
print("\n\n===============================")
