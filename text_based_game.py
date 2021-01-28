# This is a story with alternate endings and routes one can take. Each choice leads to a different outcome.
character_attributes = {'names': ['aaron', 'brandee'], 'locations': ['maui', 'rome', 'machu pichu']}
# travel = fly (don't trust cruises due to the rona)

# AARON AND BRANDEE VACATION TEXT BASED GAME

print('\nOne day, ' + ' & '.join(character_attributes['names']).title() + ' decided to go on a vacation.')
print('They had saved for a while and have chosen 3 places they would like to visit:')
for location in character_attributes['locations']:
    print('\t' + location.title())
travel = input('\n\tWill they be flying or cruising? \n<fly> or <cruise>: --> ')

if travel.lower() == 'fly':
    print('They chose to fly because nobody wants to catch the "rona" and cruiseships are incubators for that s*&%.')
elif travel.lower() == 'cruise':
    print('They chose to cruise because f**k the "rona" and fake news! Plus the ocean and pretty islands.')
else:
    print('\t<Invalid input. Choose either fly or cruise.>')



# for ROME - 1st would be colosseum, 2nd catacombs, 3rd vatican city, sistine chapel, leo davinci's secret work room
# ...try to get into bottom of pottery archeology site
# for MACHU PICHU - 1st would pet a llama, 2nd explore ancient ruins, 3rd get into lake titikaka to see the seahorses
# ...(the seahorses are from the aliens, obvi)
def rome():
    site1 = 'colosseum'
    site2 = 'catacombs'
    site3 = {'vatican city': ['sistine chapel', 'leonardo davinci secret workshop', 'pottery archeology site']}


def machu_pichu():
    site1 = 'pet a llama'
    site2 = 'explore ancient ruins'
    site3 = {'lake titicaca': 'seahorses'}
