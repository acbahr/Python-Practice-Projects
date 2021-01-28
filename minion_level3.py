"""
def n_plus(n):
    n_plus = []
    while n > 1:
        if n % 2 != 0 and n != 1:
            n = n + 1
            n_plus.append(n)
        n = n - int(n / 2)
        n_plus.append(n)
    return n_plus

def n_minus(n):
    n_minus = []
#    minus = (lambda n: n % 2 and 'odd' or 'even')
    while n > 1:
        if (n % 2 != 0) and n != 1:
            n = n - 1
            n_minus.append(n)
        n = n - int(n / 2)

        n_minus.append(n)
    return n_minus
"""
def solution(n):
    counter = []
    n = int(n)
    while n > 1:

        if n % 2 == 0:
            n = n / 2
            counter.append(int(n))
        else:
            if n == 3 or n % 4 == 1:   # % 4==1 because the next number will always be even
                n = n - 1
                counter.append(int(n))
            else:
                n = n + 1
                counter.append(int(n))
    print(counter)
    return len(counter)

print(solution('15'))

# needs to check whether n+1 or n-1 is more efficient each round

# (n-1) if (n == 3 or n % 4 == 1) else (n+1)
# if n & 1 == 0:
#      n >>= 1

print(15 % 4)
print(16/2, 8/2, 4/2, 2/2)
print(14/2, 21%4)