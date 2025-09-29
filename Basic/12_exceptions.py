

numberOne = 5
numberTwo = 1
numberTwo = "1"

try:
    print(numberOne + numberTwo)
    print("No se ah producido error")
except:
    print("Error")


try:
    print(numberOne + numberTwo)
    print("No se ah producido error")
except:
    print("Error")
else:
    print("La ejecucion continua")


try:
    print(numberOne + numberTwo)
    print("No se ah producido error")
except:
    print("Error")
else:
    print("La ejecucion continua") #Se ejecuta si no se produce la excepcion
finally:
    print("La ejecucion continua finally") #Se ejecuta siempre


#Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ah producido error")
except TypeError:
    print("TypeError")
except ValueError:
    print("ValueError")

try:
    print(numberOne + numberTwo)
    print("No se ah producido error")
except TypeError as daniel_exception:
    print(daniel_exception)
except Exception as exception:
    print(exception)