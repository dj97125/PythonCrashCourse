

my_set = set()
my_other_set = {}


print(type(my_set))
print(type(my_other_set)) # Inicialmente es un Dictionario

my_other_set = {"Brais", "MoureDev", 35}
print(type(my_other_set)) # Aqui cambia a Set

print(len(my_other_set))

print(my_other_set) #Un set no es una estructura ordenada

my_other_set.add("MoureDev") #Un Set no admite repetidos

print(my_other_set)

print("MoureDev" in my_other_set)
print("Mouri" in my_other_set)

my_other_set.remove("MoureDev")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set #Elimina my_other_set

my_set = {"Daniel","Caballero", 30}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift" , "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union({"Java", "C#"}))

print(my_new_set.difference(my_set))