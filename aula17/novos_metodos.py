# https://www.w3schools.com/python/ref_dictionary_get.asp

# The get() method returns the value of the item with the specified key.

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)

# https://www.w3schools.com/python/ref_dictionary_popitem.asp

# The popitem() method removes the item that was last inserted into the dictionary. In versions before 3.7, the popitem() method removes a random item.
# The removed item is the return value of the popitem() method, as a tuple, see example below.

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()

print(car)

# https://www.w3schools.com/python/ref_list_clear.asp

# The clear() method removes all the elements from a list.

fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()

print(fruits)