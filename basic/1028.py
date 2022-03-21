#2751
# import sys;
# n = int(sys.stdin.readline())
# a = list()

# for i in range(n):
#     a.append(int(sys.stdin.readline()))

# a.sort()

# for i in a:
#     print(i)

#11650
# import sys;
# n = int(sys.stdin.readline())
# data = [] 

# for i in range(n):
#     data.append(list(map(int, sys.stdin.readline().split())))

# data.sort()

# for i in data:
#     print(i)


#11650
# import sys
# n = int(sys.stdin.readline())
# data = []

# for i in range(n):
#     x, y  = map(int, sys.stdin.readline().split())
#     data.append([x,y])

# data.sort(key=lambda x : (x[0], x[1]))

# for i in range(n):
#     print(data[i][0], data[i][1])


#11651
# import sys
# n = int(sys.stdin.readline())
# data = []

# for i in range(n):
#     x, y  = map(int, sys.stdin.readline().split())
#     data.append([x,y])

# data.sort(key=lambda x : (x[1], x[0]))

# for i in range(n):
#     print(data[i][0], data[i][1])
