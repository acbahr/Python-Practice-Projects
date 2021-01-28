# ***********DICTIONARY IN A LIST************
# aliens.py
# We first create 3 dictionaries representing each alien, then we pack each alien into a list called 'aliens'.
# Finally we loop through the list and print out each alien.

#alien_0 = {'color': 'green', 'points': 5}
#alien_1 = {'color': 'yellow', 'points': 10}
#alien_2 = {'color': 'red', 'points': 15}

#aliens = [alien_0, alien_1, alien_2]
#for alien in aliens:
#    print(alien)

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


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# LIST IN A DICTIONARY

# consider how you might describe a pizza someone is ordering. If you were to only use a list, all you could really
# store is a list of the pizza's toppings. With a dictionary, a list of toppings can be just one aspect
# of the pizza you are describing.

# two kinds of info in the following example: crust and list of toppings
# the list of toppings is the value associated with the key 'toppings'

#pizza.py
pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}

# summarize the order
print('You ordered a ' + pizza['crust'] + ' crust pizza with the following toppings:')
for topping in pizza['toppings']:
    print('\t' + topping.upper())


# -=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# TRY YOURSELF NESTING

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three dictionaries
# in a list called people. Loop through your list of people. As you loop through the list,
# print everything you know about each person.

brandee = {'first': 'brandee', 'last': 'bahr', 'age': '46', 'city': 'lacey'}
aaron = {'first': 'aaron', 'last': 'bahr', 'age': '36', 'city': 'lacey'}
aiden = {'first': 'aiden', 'last': 'winchell', 'age': '15', 'city': 'lacey'}

people = [brandee, aaron, aiden]

for person in people:
    for key, value in person.items():
        print(key.title() + ': ' + value.title())
        if key == 'city':
            print(' ')

# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the name of a pet.
# In each dictionary, include the kind of animal and the owner's name. Store these dictionaries
# in a list called pets. Next, loop through your list and as you do print everything you know about each pet.

curtis = {'name': 'curtis', 'type': 'dog', 'owner': 'bahrs'}
steve = {'name': 'steve', 'type': 'cat', 'owner': 'bahrs'}
will_ferret = {'name': 'will ferret', 'type': 'ferret', 'owner': 'ashlee'}
pets = [curtis, steve, will_ferret]

for pet in pets:
    for key, value in pet.items():
        print(key.title() + ': ' + value.title())
        if key == 'owner':
            print(' ')

# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as
# keys in the dictionary, and store one to three favorite places for each person.
# To make this exercise a bit more interesting, ask some friends to name a few of their favorite places.
# Loop through the dictionary, and print each person's name and their favorite places.
favorite_places = {'aaron': ['paris', 'hawaii'], 'brandee': ['japan', 'germany'], 'travis': ['olympia']}
for key, value in favorite_places.items():
    if len(value) > 1:
        print("\n" + key.title() + "'s favorite places are:")
        for x in value:
            print('\t' + x.title())
    else:
        for y in value:
            print("\n" + key.title() + "'s favorite place is " + y.title())



#  6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so each person can have
# more than one favorite number. Then print each person's name along with their favorite numbers.
fav_nums = {'aaron': [8], 'brandee': [13], 'curtis': [1], 'aiden': [15], 'ashlee': [21]}
fav_nums['aaron'].append(10)
fav_nums['brandee'].append(21)

for key, value in fav_nums.items():
    if len(value) > 1:
        print("\n" + key.title() + "'s favorite numbers are:")
        for x in value:
            print('\t' + str(x))
    else:
        for x in value:
            print("\n" + key.title() + "'s favorite number is " + str(x))



# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
# Create a dictionary of information about each city and include the country that the city is in, its
# approximate population, and one fact about that city. The keys for each city's dictionary should be
# something like country, population, and fact. Print the name of each city and all of the information you have
# stored about it.
cities = {}
cities['paris'] = {'country': 'France', 'population': '10,000,000', 'fact': 'its old'}
cities['olympia'] = {'country': 'USA', 'population': '1,000,000', 'fact': 'its hippyish'}
cities['tacoma'] = {'country': 'USA', 'population': '2,000,000', 'fact': 'it smells'}
for city, city_info in cities.items():
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print('\nHere is some info on ' + city.title() + ':')
    print('It is in the country of ' + country + '.')
    print('It has a population of ' + population.title())
    print('One random fact is ' + fact + '.')


# 6-12. Extensions: We're now working with examples that are complex enough that they can be extended
# in any number of ways. Use one of the example programs from this chapter, and extend it by adding new
# keys and values, changing the context of the program or improving the formatting of the output.

