my_string = "Mi String"
my_other_string = "Mi otro String"


print(len(my_string))

print(my_other_string + " " + my_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion" 
print(my_tab_string)

my_scape_string = "\\tEste es un String  \\n escapado" 
print(my_scape_string)

name, surname, age = "Brais", "Moure", 35

print("Mi nombre es {} {} mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s mi edad es %s" %(name, surname, age))

print(f"Mi nombre es {name} {surname} mi edad es {age}")


# Desempaquetado de caracteres
language = "python"
a,b,c,d,e,f = language
print(a)
print(b)

# Division
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-3]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)


# Reverse
reversed_language = language[::-1]
print(reversed_language)

#Funciones
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("py"))
