# Loops until you type 'done'

beer_list = []
beer_list.append(input('Add a beer to the list.'))
for x in beer_list:
    if x == 'done':
        beer_list.remove('done')
        beer_list.sort()
        beers = beer_list
        print('You are done adding to the list')
        print(beers)
        print('Your list is ' + str(len(beer_list)) + ' beers long.')
    else:
        beer_list.append(input('Add another beer to the list. When finished, type "done". - '))
