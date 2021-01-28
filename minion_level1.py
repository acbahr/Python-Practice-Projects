def solution(data, n):
    # list for each task <= 99 integers
    list1 = []
#    if len(data) < 100:
#        if n == 0:
#            data.clear()
#        for num in data:
#            if data.count(num) <= n:
#                list1.append(num)
#                while num in data:
#                    data.remove(num)
    list1 = [num for num in data if data.count(num) <= n]
    return list1

print(solution([1, 2, 3, 4, 23874623, 2, 6, 7, 1, 2, 100, 99, 45], 1))
