
import os

txt_file = open("Intermediate/my_file.txt","w+") # Leer y Escribir

txt_file.write("Mi nombre es Daniel\nMi apellido es Caballero\n30 anios\nMi lenguaje Py")
# print(txt_file.read())
# print(txt_file.read(10))
# print(txt_file.readline())

for line in txt_file.readlines(): print(line)

txt_file.write("\nMe Gusta Kotlin")
print(txt_file.readline())

# txt_file.close()

with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

# os.remove("Intermediate/my_file.txt")


# Json File

import json


json_file = open("Intermediate/my_file.json", "w+")

json_test = {
    "Nombre": "Daniel",
    "Apellido": "Caballero",
    "Edad": 35,
    "Languajes": ["Python", "Swift", "Kotlin"]
    }

json.dump(json_test, json_file, indent= 4)

json_file.close()

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines(): print(line)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict ))
print(json_dict["Nombre"])

# csv file

import csv

csv_file = open("Intermediate/my_file.csv","w+") # Leer y Escribir

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Nombre", "Apellido","Edad"])
csv_writer.writerow(["Daniel", "Caballero",35])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines(): print(line)


#.xlsx file

# import xlrd #Debe instalarse el modulopara trabajar con archivos

# .xml file

import xml.etree.ElementTree as ET

xml_file = open("Intermediate/my_file.xml","w+") # Leer y Escribir

