
#  numpy

import numpy

# print(numpy.version.version)


numpy_array = numpy.array([10,24,34,44])
print(type(numpy_array))

# pandas

import pandas

import requests

response = requests.get("https://pokeapi.com/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
# print(response.json())


# Package Arithmetics

from my_package import arithmetics

print(arithmetics.sum_two_values(2,2))