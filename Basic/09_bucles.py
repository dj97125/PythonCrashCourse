

# While


my_condition = 0


while my_condition < 10:
    print(my_condition)
    my_condition += 1
else: # Es opcional
    print("Condicion mayor o igual que 10")


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break

# For
my_list = [35, 24, 77, 17, 30, 30]

for element in my_list:
    print(element)


my_tuple = (32, 1.77, "Daniel", "Caballero")

for element in my_tuple:
    print(element)

my_set = {"Daniel","Caballero", 30}

for element in my_set:
    print(element)


my_dict = {
    "Nombre": "Daniel",
    "Apellido" : "Caballero", 
    "Edad": 35, 
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1 : 1.70
    }

for element in my_dict:
    print(element)
    if element == "Edad":
        print("Tengo Edad")
        break
else:
    print("Bucle para diccionario finalizado")

for element in my_dict:
    print(element)
    if element == "Edad":
        print("Tengo Edad")
        continue
else:
    print("Bucle para diccionario finalizado")


for element in my_dict.values():
    print(element)
else:
    print("Bucle finalizado")



print("La ejecucion continua")