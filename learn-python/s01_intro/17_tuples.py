# tuples

simple_tuple = "Rolf", "Bob"
print(simple_tuple)

# brackets are recommended
clear_tuple = ("Rolf", "Bob")
print(clear_tuple)

# brackets are required in lists of tuples
tuple_in_list = [("Rolf", "Bob")]
print(tuple_in_list)

# tuple object has no attribute 'append'
friends = ("Rolf", "Bob", "Anne")
print(friends)

# friends.append("Jen") > AttributeError: 'tuple' object has no attribute 'append'
# When you use an equal sign, the right side evaluates first.
friends = friends + ("Jen", )
print(friends)
