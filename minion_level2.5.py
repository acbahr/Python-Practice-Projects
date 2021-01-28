# step 1
# n = random minion ID with k(len(n))
# b = base (1211 is base 10(all digits 0-9))
# base 3 -> digits are 0,1,2
# step 2
# x = 2111 (descending)
# y = 1112 (ascending)
# step 3
# z = x - y (if len < k, add leading zero)
# example - 0999 = 2111-1112
# step 4
# n = z to get minion ID and go back to step 2
import math


# convert base b to decimal
def baseb_to_decimal_conversion(number, base):
#    if int(number) == 0:
#        return '0'
#    else:
    decimal_number = 0
    i = 0
    while (number != 0):
        number, remainder = divmod(int(number), 10)
        decimal_number += remainder * math.pow(base, i)
        i += 1
#    print(number, 'converted to decimal', int(decimal_number))
    return str(int(decimal_number))


# convert decimal to base b
def decimal_to_baseb_conversion(num, b):
#    if num == 0:
#        return '0'
    nums = []
    while num:
        num, r = divmod(int(num), b)
        nums.append(str(r))

#    print(num, 'converted to ', ''.join(reversed(nums)))
    return ''.join(reversed(nums))


def solution(n, b):
    list1 = []
    k = len(n)
    m = n

    while m not in list1:
        list1.append(m)
        x_desc = ''.join(sorted(m, reverse=True))
        y_asc = ''.join(sorted(m))
        print(x_desc)
        print(y_asc)
        if b == 10:
            m = str(int(x_desc) - int(y_asc))

        else:
            z = int(baseb_to_decimal_conversion(x_desc, b)) - int(baseb_to_decimal_conversion(y_asc, b))
            m = decimal_to_baseb_conversion(str(z), b)
            print(z)
        m = (k - len(m)) * '0' + m

    return (len(list1) - list1.index(m))

x = 1236314
n = 9
y = decimal_to_baseb_conversion(x, n)
z = baseb_to_decimal_conversion(y, n)
print(y)
print(z)
print(str(x) == z)

print(solution('210022', 3))