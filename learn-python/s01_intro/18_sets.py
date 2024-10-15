# sets
# sets don't hold other and they don't contain duplicates

art_friends = {"Rolf", "Anne"}
art_friends.add("Jen")
print(art_friends)

# nothing gets added to this set
art_friends.add("Jen")
print(art_friends)

# Jen gets removed
art_friends.remove("Jen")
print(art_friends)
