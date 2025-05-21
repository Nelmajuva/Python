textOne = "Hello,"
textTwo = "World"

textThree = """
    Hello,
    Mi name is Juan Camilo López Morales
"""

print(textOne + ' ' + textTwo)
print(textThree)

# String Formatting

welcome = f'{textOne} {textTwo}'

print(welcome)

# String Indexes

print(welcome[5])
print(welcome[len(welcome) - 1])
print(welcome[-1])
print(welcome[:5])

# String Indexes - Example Reverse Text

print(welcome[::-1])