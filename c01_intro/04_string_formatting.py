# Multi-variable f-string
user = "Rolf Smith"
street = "123 No Name Road"
postcode = "PY10 1CP"

address = f"""User: {user}
Street: {street}
Postcode: {postcode}
Country: United Kingdom"""
print(address)

# Using named format
named_template = "Hello {name}"
named_greeting = named_template.format(name = "Moto")
print(named_greeting)

# Using format
template = "Hello, {}"
greeting_042 = template.format("042")
print(greeting_042)

greeting_153 = template.format("153")
print(greeting_153)

# Using f-strings
name = "Pod"
greeting = f"How are you, {name}?"
print(greeting)

# The same greeting gets printed twice because f-strings do not take changes over variable `name`.
name = "Bob"
print(greeting)