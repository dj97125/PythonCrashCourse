
import re

my_string = "Leccion 7: leccion Expressiones Regulares"
my_other_string = "Leccion 6: Manejo de ficheros"


match = re.match("Leccion",my_string, re.I)
print(match)
start, end = match.span()
print(f"span from: {start} to {end}")
print(my_string[start:end])

match = re.match("Leccion",my_string, re.I)
# if not(match == None):
# if match is not None):
if match != None:
    print(match)
    start, end = match.span()
    print(my_string[start:end])


# search

search = re.search("Expressiones",my_string, re.I)
print(search)
start, end= search.span()
print(my_string[start:end])

# Findall

findall = re.findall("Leccion",my_string, re.I)
print(findall)


# Split

print(re.split(":", my_string))

# Sub

print(re.sub("Expressiones", "expressiones", my_string))
print(re.sub("Leccion|leccion", "LECCION", my_string))
print(re.sub("[L|l]eccion", "LECCION", my_string))


# Patterns

pattern = r"[Ll]eccion"
print(re.findall(pattern, my_string))

pattern = r"[Ll]eccion|Expressiones"
print(re.findall(pattern, my_string))

pattern = r"[a-z0-9]"
print(re.findall(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l]"
print(re.findall(pattern, my_string))

email = "mouredev@mouredev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email))


