# sets
# sets don't hold other, and they don't contain duplicates

art_friends = {"Rolf", "Anne"}
art_friends.add("Jen")

# nothing gets added to this set
art_friends.add("Jen")

# Jen gets removed
art_friends.remove("Jen")
art_friends.add("Jen")
science_friends = {"Jen", "Charlie"}

print("art friends....:", art_friends)
print("science friends:", science_friends)

art_but_not_science = art_friends.difference(science_friends)
print("art only.......:", art_but_not_science)

science_but_not_art = science_friends.difference(art_friends)
print("science only...:", science_but_not_art)

# symmetric difference: members that aren't in both sets
not_in_both = art_friends.symmetric_difference(science_friends)
print("not in both....:", not_in_both)

in_both = art_friends.intersection(science_friends)
print("in both........:", in_both)

all_friends = art_friends.union(science_friends)
print("all friends....:", all_friends)
