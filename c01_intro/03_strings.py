single_quotes = "Hello, it's me"
print(single_quotes)

double_quotes = 'She said: "You are amazing"'
print(double_quotes)

escaping_quotes = "She said: \"Hello\""
print(escaping_quotes)

multiline = """Hello.
My name is pod042.
"""
print(multiline)

"""
Comments:
Multi-line strings can be useful for long comments.
Basically, we created a string and then... that's it.
"""
name = "pod"
greeting = "Hello, " + name
print(greeting)

"""
Comments:
We're converting an integer into string before printing it.
"""
id = 1100
id_as_str = str(1100)
print("Customer ID: " + id_as_str)