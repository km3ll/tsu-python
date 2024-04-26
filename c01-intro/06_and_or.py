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

# Falsy value with OR expression can be used for defaults
default_greeting = 'there'
name = input('Enter your name: (optional) ')
user_name = name or default_greeting
print(f'Hello, {user_name}!')
