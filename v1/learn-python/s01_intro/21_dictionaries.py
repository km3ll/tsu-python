# dictionaries
# a dictionary stores keys and values
# - it keeps insertion order
# - it contains unique keys

friends_and_ages = {
    "Rolf": 24,
    "Adam": 30,
    "Anne": 27
}
print("Dictionary:", friends_and_ages)

# getting
print("Rolf's age:", friends_and_ages["Rolf"])

# setting
friends_and_ages["Bob"] = 20
print("Dictionary:", friends_and_ages)

# changing
friends_and_ages["Rolf"] = 25
print("Rolf's new age:", friends_and_ages["Rolf"])

# tuple of dictionaries
friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
)
print("friends......:", friends)
print("friend's name:", friends[0]["name"])

friend = friends[0]
print("friend's name:", friend["name"])

# dict: convert list into a dictionary
more_friends = [("Rolf", 34), ("Adam", 30), ("Anne", 27)]
dict_friends = dict(more_friends)
print("dict friends.:", dict_friends)
