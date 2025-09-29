# Tuples are inmutables whereas the list are 


my_tuple = tuple()
my_other_tuple = ()


my_tuple = (32, 1.77, "Daniel", "Caballero")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Daniel"))
print(my_tuple.index("Daniel"))

# my_tuple[1] = 1.80
# print(my_tuple)  #TypeError

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "Moure"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(type(my_tuple))

del my_tuple
# print(my_tuple) NameError: name "my_tuple" is not defined
