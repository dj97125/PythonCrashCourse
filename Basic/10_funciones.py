

def my_function ():
    print("Esto es una funcion")

my_function()

def sum_two_values(first_number, second_number):
    print(first_number + second_number)

sum_two_values(first_number = 2, second_number = 2)

def sum_two_values_with_return(first_number, second_number):
   return first_number + second_number

print(sum_two_values_with_return(first_number= 4, second_number= 6))


def print_name(name, surname): print(f"{name} {surname}")

print_name(name = "Daniel", surname="Caballero")

def print_name_with_default (name, surname, alias = "Sin alias"): print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure")

def print_upper_texts(*texts): 
    for element in texts: print(element.upper())

print_upper_texts("Hola", "Python", " ", "Daniel")