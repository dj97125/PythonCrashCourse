

# class MyEmptyyPerson: 
#     pass 


# print(MyEmptyyPerson())

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.name = name
        self.surname = surname
        self.full_name = f"{name} {surname}" #Propiedad publica
        self.__alias = f"{name} {surname} {alias}" #Propiedad privada

    def get_alias (self): return self.__alias

    def walk(self): print(f"{self.full_name} Estoy caminando")

my_person = Person(name = "Daniel", surname = "Caballero")
print(f"{my_person.name} {my_person.surname}")
print(my_person.full_name)
my_person.walk()

my_other_person = Person(name = "Manuel", surname = "Caballero", alias = "Dani")
print(f"{my_other_person.name} {my_other_person.surname}")
print(my_other_person.full_name)
# print(my_other_person.__alias) # Error: No puedo acceder a __alias por que es privado del methodo
print(my_other_person.get_alias())
my_other_person.walk()