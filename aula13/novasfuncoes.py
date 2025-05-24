# https://www.w3schools.com/python/ref_random_choice.asp

# The choice() method returns a randomly selected element from the specified sequence.

import random

mylist = ["apple", "banana", "cherry"]

print(random.choice(mylist))

# The enumerate function is used in for loops to provide an index for each item in a sequence, like a list or a string. This makes it easy to track the position of each element in the loop, in addition to accessing the element's value.

fruits = ["apple", "banana", "cherry", "orange"]

# Loop with enumerate to get both the index and the value of each item
for index, fruit in enumerate(fruits):
    print(f"Fruit {index + 1}: {fruit}")
    
# If we iterate over a list in a for loop without enumerate, we access only the value of each item, but not the index of each element. This is useful when we only need the value and not its position in the list.

fruits = ["apple", "banana", "cherry", "orange"]

# Loop without enumerate, where we only get the value of each item
for fruit in fruits:
    print(f"Fruit: {fruit}")