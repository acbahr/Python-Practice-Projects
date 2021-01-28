import math

# converts 102212 from base 3 to base 10
#base10 = (1*3**5) + (0*3**4) + (2*3**3) + (2*3**2) + (1*3**1) + (2*3**0)
#print(base10)


# convert base 10 to base 3
def decimal_to_baseb_conversion(num, b):
    if num == 0:
        return '0'
    nums = []
    while num:
        num, r = divmod(int(num), b)
        nums.append(str(r))
    return ''.join(reversed(nums))

# ---OR---
def any_base_conversion(number, base):
    e = number // base
    q = number % base
    if number == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return any_base_conversion(e, base) + str(q)
# ---OR---


#print(decimal_to_baseb_conversion(320, 3))
# print(math.log(102212, 3))
# print(3**10.499431406026561)

# converting a number to base 10
def baseb_to_decimal_conversion(number, base):
    if int(number) == 0:
        return '0'
    else:
        decimal_number = 0
        i = 0
#        remainder = 0
        while (number != 0):
            number, remainder = divmod(int(number), 10)
            decimal_number += remainder * math.pow(base, i)
            i += 1
        return int(decimal_number)

def baseb_to_decimal_conversion3(number, base):
#    x = list(sorted(number, reverse=True))
    x = list(number)
    decimal_number = 0

    for i, a in enumerate(x):
        decimal_number += int(a) * (base ** i)

    return decimal_number
#print(baseb_to_decimal_conversion(102212, 3))

def solution(n, b):
    print('input n:', n)
    list1 = []

    while True:
        if list1.count(n) > 1:
            print(list1)
            count = [x for x in list1 if x != n]
            return 1 if list1[-1:] == list1[-2:-1] else len(count)

        k = len(n)
        x = int(''.join(sorted(n, reverse=True)))
        y = int(''.join(sorted(n)))
        print('x: ' + str(x) + ' y: ' + str(y) + ' k: ' + str(k))

        if b != 10:
            x = baseb_to_decimal_conversion(x, b)   # converts x to decimal
            y = baseb_to_decimal_conversion(y, b)   # converts y to decimal
            z = str(decimal_to_baseb_conversion((x - y), b)).zfill(k)   # convert back to b and adds leading 0 to len k
            print('if:', z)
#            count += 1
            list1.append(z)
            n = z

        else:
            z = str(x - y).zfill(k)
#            count += 1
            list1.append(z)
            print('else:', z)
            n = z


print(decimal_to_baseb_conversion('320', 3))
print(baseb_to_decimal_conversion('210022', 3))
