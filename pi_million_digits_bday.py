with open('text_files/pi_million_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + '...')
print(len(pi_string))


def birthday_pi():
    birthday = input('Enter your birthday in the form of mmddyy: ')
    if birthday in pi_string:
        index = pi_string.index(birthday)
        index_line = index / 100
        print('Your birthday is in the first million digits of PI at index '
              + str(index) + ' at line ' + str(round(index_line)) + '!')
    else:
        print('Your birthday is not in the first million digits of PI.')


birthday_pi()

