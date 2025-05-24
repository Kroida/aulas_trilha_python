# https://www.w3schools.com/python/ref_keyword_pass.asp

# The pass statement is used as a placeholder for future code.

# When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.

# Empty code is not allowed in loops, function definitions, class definitions, or in if statements.

for x in [0, 1, 2]:
  pass

# https://www.w3schools.com/python/gloss_python_raise.asp

# The raise keyword is used to raise an exception.

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")