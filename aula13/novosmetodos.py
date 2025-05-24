# https://www.w3schools.com/python/ref_string_join.asp

# The join() method takes all items in an iterable and joins them into one string.

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

# Basically, join is a "sep" for lists

y = ' '.join(myTuple)

print(y)

# ---
import random

palavras = ['python', 'algoritmo', 'programacao', 'forca', 'educacao', 'tecnologia']

palavra_secreta = random.choice(palavras)

letras_descobertas = ['_' for _ in palavra_secreta]

print(letras_descobertas)

# https://www.w3schools.com/python/ref_string_isalpha.asp

# The isalpha() method returns True if all the characters are alphabet letters (a-z).

txt = "CompanyX"

x = txt.isalpha()

print(x)

# https://www.w3schools.com/python/ref_list_pop.asp

# The pop() method removes the element at the specified position.

fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

print(fruits)