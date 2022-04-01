# n, m = map(int, input().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int,input())))

# def dfs(x, y):
#     if x<=-1 or x>=n or y <= -1 or y >= m:
#         return False
    
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x-1,y)
#         dfs(x,y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
#         return True
    
#     return False


# result = 0

# for i in range(n):
#     for j in range(m):
#         if dfs(i,j) == True:
#             result += 1
#             print('dfs(i,j)',i,j,'result',result)

# print(result)


# import random

# li = [1,2,3]
# choiceList = random.choice(li)


# items = ['1','2','3','4','5']
# from itertools import combinations, permutations
# print(list(permutations(items,2)))
# print(list(combinations(items,2)))


# array = [5,7,9,0,3,1,6,2,4,8]

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
    
#     pivot = array[0]
#     tail = array[1:]

#     left_side = [x for x in tail if x <= pivot]
#     right_side = [x for x in tail if x > pivot]
#     print(left_side)
#     print(right_side)
#     return True

# quick_sort(array)

# array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# count = [0] * (max(array) + 1)

# for i in range(len(array)):
#     count[array[i]] += 1

# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i, end=' ')


# n = int(input())
# data =[]
# for i in range(n):
#     data.append(int(input()))

# data.sort()
# data.reverse()
# print(data)


# n = int(input())

# array = []
# for i in range(n):
#     input_data = input().split()
#     array.append((input_data[0],input_data[1]))

# array = sorted(array, key=lambda student:student[1])

# for student in array:
#     print(student[0], end='')


# n, k =map(int, input().split())

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# a.sort()
# b.sort()

# for i in range(k):
#     a[i],b[-i] = b[-i],a[i]

# print(a)
# print(b)
# print(sum(a))

