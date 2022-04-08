# p99 1이 될때까지
# n, k = map(int,input().split())
# cnt = 0

# while n != 1:
#     if n % k == 0:
#         n = n // k
#         cnt += 1
#     else :
#         n -= 1
#         cnt += 1
# print(cnt)


# p110 상하좌우
# n = int(input())
# plans = input().split()
# x, y = 1,1

# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# mtypes = ['L','R','U','D']

# for plan in plans:
#     for i in range(len(mtypes)):
#         if plan == mtypes[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     # print(x, y,nx,ny)
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue

#     x, y = nx, ny
# print(x,y)




# p113 시각
# n = int(input())
# cnt = 0
# for i in range(n + 1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 cnt += 1
# print(cnt)


# p115 왕실의 나이트
# loc = input()
# row = int(loc[1])
# col = int(ord(loc[0])) - int(ord('a')) + 1

# steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

# result = 0
# for step in steps:
#     nrow = row + step[0]
#     ncol = col + step[1]
    
#     if nrow >= 1 and nrow <= 8 and ncol >= 1 and ncol <= 8:
#         result += 1

# print(result)


# stack
# stack = []

# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop()
# stack.append(1)
# stack.append(4)
# stack.pop()

# print(stack)
# print(stack[::-1])

#queue
# from collections import deque

# queue = deque()

# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()

# print(queue)
# queue.reverse()
# print(queue)

# DFS
# def dfs(graph, v, visited):
#     visited[v] = True
#     print('v의 값',v,'일 때 graph[v]의 값',graph[v])
#     # print(v)
#     # print(graph[v])
#     for i in graph[v]:
        
#         print('아직 포문 안?',graph[v],'인접 인 노드',i,'중')
#         if not visited[i]:
#             print('아직 가지 않은', i)
#             print('++')
#             dfs(graph, i, visited)
#         print('--')
#     print('v = ',v,'포문 벗어나기')
            
# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]

# visited = [False] * 9

# dfs(graph, 1, visited)


# BFS

# from collections import deque

# def bfs(graph, start, visited):
#     queue = deque([start])
#     print('queue = ',queue)
#     visited[start] = True

#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]

# visited = [False] * 9

# bfs(graph, 1, visited)

# 선택정렬
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(len(array)):
#     min_idx = i
#     for j in range(i+1, len(array)):
#         if array[min_idx] > array[j]:
#             min_idx = j
#     array[i], array[min_idx] = array[min_idx], array[i]

# print(array)

# 스와이프
# array = [3,5]
# array[0], array[1] = array[1],array[0]

# print(array)

# 삽입정렬
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(1, len(array)):
#     for j in range(i,0,-1):
#         if array[j] < array[j-1]:
#             array[j], array[j-1] = array[j-1], array[j]
#         else : 
#             break
# print(array)