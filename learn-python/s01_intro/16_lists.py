friends = ['Rolf', 'Anne', 'Mike']

# Original list
print(f'Friends: {friends}')
# First and Last elements
print(f'\nFirst: {friends[0]}')
print(f'\nLast: {friends[-1]}')

# Reverted list
print(f'\nReverted: {friends[::-1]}')

# List size
print(f'\nFriends count: {len(friends)}')

# Friends and ages
friends_and_ages = [
    ['Rolf', 24],
    ['Anne', 30],
    ['John', 31],
    ['Mike', 27]
]
print("\nRolf's age is:", friends_and_ages[0][1])
print("\nMike's age is:", friends_and_ages[-1][1])

# Adding and removing
amigos = ['Rolf', 'Bob', 'Anne']
print('\nAmigos:', amigos)
amigos.append('Jen')
print('  .append("Jen"):', amigos)
amigos.remove('Bob')
print('  .remove("Bob"):', amigos)

amigos_y_edades = [
    ['Rolf', 24],
    ['Anne', 30],
    ['John', 31],
    ['Mike', 27]
]

print('\nAmigos y edades:', amigos_y_edades)
amigos_y_edades.remove(['Rolf', 24])
print('  .remove[\'Rolf\', 24]:', amigos_y_edades)
