

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Daniel", "Apellido" : "Caballero", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre": "Daniel",
    "Apellido" : "Caballero", 
    "Edad": 35, 
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1 : 1.70
    }

print(my_dict)
print(my_other_dict)

print(my_dict["Lenguajes"])

my_dict["Calle"] = "Calle San Juan"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Apellido" in my_dict)
print("Daniel" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())


my_new_dict = dict.fromkeys(("Nombre",1))
my_new_dict["Nombre"] = "Daniel"
print(my_new_dict)
