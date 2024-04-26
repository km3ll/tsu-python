friends = ['Rolf', 'Anne', 'Mike']

# Original list
print(f'Friends: {friends}')
# Reverted list
print(f'My Friends: {friends[::-1]}')

# First and Last elements
print(f'First: {friends[0]}')
print(f'Last: {friends[-1]}')

# List size
print(f'Friends count: {len(friends)}')

# List of friends and ages
friends_and_ages = [
    ['Rolf', 24],
    ['Anne', 30],
    ['John', 31],
    ['Mike', 27]
]

print("Rolf's age is:", friends_and_ages[0][1])
print("Mike's age is:", friends_and_ages[-1][1])

# Adding and removing
more_friends = ['Rolf', 'Bob', 'Anne']
print('Friends:', more_friends)
more_friends.append('Jen')
print('Friends .append("Jen"):', more_friends)
more_friends.remove('Bob')
print('Friends .remove("Bob"):', more_friends)

more_friends_and_ages = [
    ['Rolf', 24],
    ['Anne', 30],
    ['John', 31],
    ['Mike', 27]
]

print('More friends and ages:', more_friends_and_ages)
more_friends_and_ages.remove(['Rolf', 24])
print('.remove[\'Rolf\', 24]:', more_friends_and_ages)
