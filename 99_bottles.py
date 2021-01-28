# 1. Create a program that prints out every line to the song "99 bottles of beer on the wall."
# 2. Do not use a list for all of the numbers, and do not manually type them all in.
#    Use a built in function instead.
# 3. Besides the phrase "take one down," you may not type in any numbers/names of numbers
#    directly into your song lyrics.
# 4. Remember, when you reach 1 bottle left, the word "bottles" becomes singular.


def beer_song():
    bottle_count = 99

    while bottle_count >= 2:

        print('\n' + str(bottle_count) + ' bottles of beer on the wall, ' + str(bottle_count) + ' bottles of beer.')
        bottle_count = bottle_count - 1

        if bottle_count > 1:
            print('Take one down, pass it around, ' + str(bottle_count) + ' bottles of beer on the wall.')
        else:
            print('Take one down, pass it around, ' + str(bottle_count) + ' bottle of beer on the wall.')

    if bottle_count == 1:

        print('\n' + str(bottle_count) + ' bottle of beer on the wall, ' + str(bottle_count) + ' bottle of beer.')
        print('Take it down, pass it around, no more bottles of beer on the wall.')


beer_song()
