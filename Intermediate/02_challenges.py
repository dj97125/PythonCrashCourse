
# FIZZ BUZZ

def fizzbuzz():
    for index in range(1,101):
        if index % 3 == 0 and index % 5 == 0: print("fizzbuzz")
        elif index % 3 == 0: print("fizz")
        elif index % 5 == 0: print("buzz")
        else: print(index)

fizzbuzz()

# Es un Anagrama?

def is_anagram(word_one: str, word_two):
    
    if word_one.lower() == word_two.lower():
        return False
    
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(f"isAnagram? {is_anagram("Amora", "rOMA")}")


# Sucession de fibonacci con los primeros 50 numeros

def fibonacci():

    prev = 0
    next = 1

    for index in range(0,50):
        print(prev)

        fib = prev + next
        prev = next
        next = fib

fibonacci()

# Es un numero primo?

def is_prime(): 
        for number in range(1,101):
            if number >= 2:
                is_divisible = False
            
                for index in range(2, number):
                    if number % index == 0:
                        is_divisible = True
                        break
                
                if is_divisible:
                    print(f"isPrime {number}")
    

is_prime()

"""
Invertir Cadenas de Texto

Crea un programa que invierta el orden de una cadena de texto si usar funciones propias del lenguaje que lo 
hagan de forma automatica. 

 - Si le pasamos "Hola Mundo" retornaria "odnum aloH"

"""


def reverse(text: str):
    reversed_text = ""
    text_len = len(text) -1

    for index in range(0, (text_len + 1)):
        reversed_text += text[text_len - (index)]

    return reversed_text


print(reverse("Hola Mundo"))
