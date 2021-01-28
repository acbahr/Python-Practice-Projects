# 1. Learn about armstrong numbers here. A.K.A. narcissistic number
# 2. Define a function that allows the user to check whether a given number is armstrong number or not.
# 3. Hint: To do this, first determine the number of digits of the given number.
#    Call that n. Then take every digit in the number and raise it to the nth power.
#    Add them, and if your answer is the original number then it is an Armstrong number.
# 4. Example: Take 1634. Four digits. So, 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634.
#    So 1634 is an Armstrong number.
# 5. Tip: All single digit numbers are Armstrong numbers.
import math


def armstrong_number(n):
    num_len = len(str(n))
    num_list = list(str(n))
    sum_list = []
    for x in num_list:
        sum_list.append(math.pow(int(x), num_len))

    return int(sum(sum_list)) == n


print(armstrong_number(1634))

'''
def grid_paths(n, m):
    if n == 1 or m == 1:
        return 1
    else:
        return grid_paths(n, m - 1) + grid_paths(n - 1, m)

print(grid_paths(3, 4))
'''
