alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# a more realistic example would involve more than 3 aliens with code that automatically generates
# each alien. In the following example we use range() to create a fleet of 30 aliens.
# Making an empty list for storing aliens

aliens = []
# make 30 green aliens
# for alien_number in range(30) tells Python how many times we want the loop to repeat, thus adding 30 aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# show the first 5 aliens:
# using slice to print the first 5 aliens
for x in aliens[:5]:
    print(x)
print('...')

# show how many aliens have been created to prove 30 have been created:
print(str(len(aliens)) + ' aliens have been created')

# to edit the list and change the first 3 to yellow:
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)
print('...')

for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:7]:
    print(alien)
print('...')
