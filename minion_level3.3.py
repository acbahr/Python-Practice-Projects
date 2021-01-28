from math import floor, sqrt
"""
def solution(n):
    # n == total number of bricks
    # n! / r!(n-r)! where r is number chosen
    # ex-16 pool balls how many combos of 3 can be done
    # 16! / 3!(16-3)! == 560 permutations w/o repetition


    if n < 3 or n > 200:
        return 0
    else:
        sum = 0
        cache = []
        for x in range(0, n):
            list1 = []
            for y in range(0, n):
                list1.append(-1)
            cache.append(list1)

    for i in range(int(floor(sqrt(n*2))), n):
        sum += recurse(n - 1, i, cache)
#    print(staircases)
    return sum

def recurse(remaining, previous, cache):
    if remaining == 0:
        return 0
    if previous == 1:
        return 0

    if cache[remaining][previous] != -1:
        return cache[remaining][previous]

    sum = 0
    if previous > remaining:
        sum += 1
    for i in range(int(floor(sqrt(remaining*2))), remaining):
        if i >= previous:
            break
        sum += recurse(remaining - i, i, cache)
    cache[remaining][previous] = sum
    return sum
"""

def staircase(h, l, memo):
    if memo[h][l] != 0:
        return memo[h][l]
    if l == 0:
        return 1
    if l < h:
        return 0
    memo[h][l] = staircase(h + 1, l - h, memo) + staircase(h + 1, l, memo)
    return memo[h][l]


def answer(n):

    memo = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    return staircase(1, n, memo) - 1


print(answer(200))