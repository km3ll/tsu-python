age = int(input('Enter your age: '))
result_1 = age > 18 and age < 65
result_2 = 18 >= age <= 65
print('Your age is within the range:', result_2)

# Evaluating empty values with bool() function
print("Numbers:")
print("bool(0)", bool(0))
print("bool(12)", bool(12))

print('Strings: ')
print("bool('')", bool(''))
print("bool('Hello')", bool('Hello'))

print('Lists: ')
print("bool([])", bool([]))
print("bool([2, 4, 6])", bool([2, 4, 6]))

# The `or` keyword gives us the second value if the first one is falsy.
default_greeting = 'there'
name = input('Enter your name: (optional) ')
user_name = name or default_greeting
print(f'Hello, {user_name}!')

# The `and` keyword gives us the second value if the first one is truthy.
x = True
cmp = x and 18
print('cmp value: ', cmp)

# Keywords `and` and `or` have the same priority and evaluate left to right when in one line.
age = 16
side_job = True
print(age > 18 and age <65 or side_job)
# The conditionals evaluate first, and then `and` and `or` evaluate left to right.
# That means that we are evaluating `False and True or True`.
# Since we evaluate left to right, `False and True` give us `False`.
# We are left with `False or True`, which gives us `True`.

