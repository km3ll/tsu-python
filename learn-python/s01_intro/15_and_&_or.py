# and & or
age = 30
within_range = 18 < age < 65
print('Age within range:', within_range)

# Evaluating empty values with bool()
print("\nNumbers:")
print("- bool(-10)", bool(-10))
print("- bool(0)", bool(0))
print("- bool(10)", bool(12))

print('\nStrings:')
print("- bool('')", bool(''))
print("- bool(' ')", bool(' '))
print("- bool('Hello')", bool('Hello'))

print('\nLists:')
print("- bool([])", bool([]))
print("- bool([2, 4, 6])", bool([2, 4, 6]))

# The 'and' keyword gives us the second value if the first one is truthy.
x = False
compared_and = x and 18
print('\nCompared "and":', compared_and)

default_age = 30
y = 0
compared_or = y or default_age
print('\nCompared "or":', compared_or)

# Keywords 'and' and 'or' have the same priority and evaluate left to right when in one line.
age = 16
side_job = True
print(18 < age < 65 or side_job)
# The conditionals evaluate first, and then 'and' and 'or' evaluate left to right.
# That means that we are evaluating 'False and True or True'.
# Since we evaluate left to right, 'False and True' give us 'False'.
# We are left with 'False or True', which gives us 'True'.

# The 'or' keyword gives us the second value if the first one is falsy.
default_greeting = 'there'
user_input = input('\nEnter your name: (optional) ')
name = user_input or default_greeting
print(f'Hello, {name}!')
