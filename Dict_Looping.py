# LOOPING THRU A DICTIONARY
# user.py

user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)

print(' ')

favorite_lang = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
for name, fav in favorite_lang.items():
    print(name.title() + "'s favorite language is " + fav.title() + ".")

print(' ')

# Using .keys() and .values() methods to loop through just the keys or values
# Use set() function for values to remove repeated values
for name in sorted(favorite_lang.keys()):
    print(name.title())
print(' ')
for value in set(favorite_lang.values()):
    print('The chosen languages are ' + value.title())

print(' ')

# Special message for chosen keys
friends = ['phil', 'sarah']
# Use the sorted() function to sort the dictionary output in alphabetical order.
for name in sorted(favorite_lang.keys()):
    print(name.title())
    if name in friends:
        print("Hello " + name.title() + ", I see your favorite language is " + favorite_lang[name].title())

# .keys() method not just for looping. It returns a list of all keys in dictionary and the IF statement
# below checks the input against all the keys.
entrant = str(input('Type your name here: - '))
if entrant.lower() not in favorite_lang.keys():
    print('Hello, ' + entrant.title() + ', please take the poll!')

print('\n')
# =========================================
# TRY YOURSELF


glossary = {}
glossary['tuple'] = 'immutable(unchangeable) list surrounded by () instead of []'
glossary['dictionary'] = 'a list of key/value pairs'
glossary['IF statement'] = 'conditional test of input'
glossary['elif'] = 'conditional continuation of IF statements'
glossary['range'] = 'function that you already know, but add 1 to the end'
glossary['str'] = 'function that changes item to a string'
glossary['set'] = 'function that looks through dictionary and removes repeats'
glossary['sorted'] = 'function that arranges dictionary output alphabetically'
glossary['keys.() method'] = 'returns the keys of a dictionary'
glossary['values.() method'] = 'returns the values of a dictionary'

for key, value in glossary.items():
    print(key + ': ' + value)

print(' ')
# Rivers.py - Make a dictionary containing 3 major rivers and the country each river runs thru.

rivers = {'nile': 'egypt', 'amazon': 'congo', 'potomac': 'usa'}

for key, value in rivers.items():
    print('The ' + key.title() + ' runs through ' + value.title() + '.')

for value in rivers.values():
    print(value.title())
for key in rivers.keys():
    print(key.title())

print(' ')

favorite_lang = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
pollers = ('jen', 'sarah', 'aaron', 'brandee', 'tim', 'travis', 'chad')

for user in pollers:
    if user in favorite_lang.keys():
        print('Hello ' + str(user.title()) + ', you have already taken the poll and answered ' +
              favorite_lang[user].title() + '.')
    else:
        print('Hello ' + str(user.title()) + ', please take a moment to finish the poll.')

print('\nList of those who have not taken the poll:')
for x in pollers:
    if x not in favorite_lang.keys():
        print(x.title())
