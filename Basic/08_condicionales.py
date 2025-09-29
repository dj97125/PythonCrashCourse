
my_condition = True

if my_condition:
    print("Ejecuta el if")

my_condition = 5 * 2

if my_condition == 11:
    print("Ejecuta el segundo if")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 1:
    print("Es igual que uno")
else:
    print("Es menor que 10 y mayor que 20")

my_string = "H"

if not my_string:
    print("Texto vacio")
else:
    print("No Vacio")


print("La ejecucion continua")