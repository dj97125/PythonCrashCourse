
from functools import reduce

# HIGHER ORDER FUNCTIONS

def sum_one(vallue): return vallue + 1

def sum_five(vallue): return vallue + 5


def sum_two_values_and_add_one_function(first_value, second_value, f_sum): return f_sum(first_value + second_value)

print(sum_two_values_and_add_one_function(5,2, sum_one))
print(sum_two_values_and_add_one_function(5,2, sum_five))

def sum_ten():
    def add(value):
        return value + 10
    return add


add_closure = sum_ten() 
print(add_closure(value = 5))

def sum_ten_2(higher_value):
    def add(value):
        return value + 10 + higher_value
    return add

add_closure = sum_ten_2(higher_value = 2) 
print(add_closure(value = 5))

print(sum_ten_2(higher_value = 2)(value = 5))


# BUILT-IN HIGHER ORDER FUNCTIONS

numbers = [2,5,10,21,30]

# Map

def multiply_two(number): return number * 2

print(map(multiply_two, numbers))

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter

def filter_greater_than_ten(number):
    if number > 10: return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce

def sum_two_values(first_value, second_value): 
    print(f"first_value = {first_value}, second_value = {second_value}")

    return first_value + second_value


print(reduce(sum_two_values,numbers))

print(reduce(lambda first_value, second_value: first_value + second_value ,numbers))