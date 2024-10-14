# f-strings
name = "042"
greeting = f"How are you, {name}?"
print(greeting)

"""
The same greeting is printed twice.
Variable 'greeting' is not updated with name 'John'
"""
name = "153"
print(greeting)

# format
template1 = "Hello, {}"
greeting1 = template1.format("042")
print(greeting1)

# format with name
template2 = "Hello, {name}"
greeting2 = template2.format(name="153")
print(greeting2)

# multi-variable f-string
user = "Rolf Smith"
street = "123 No Name Road"
postcode = "PY10 1CP"

address = f"""User: {user}
Street: {street}
Postcode: {postcode}
Country: United Kingdom"""
print(address)
