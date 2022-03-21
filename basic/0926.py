#11721
# sentenc = input()
# for i in range(len(sentenc)):
#     print(sentenc[i], end='')
#     if i % 10 == 9:
#         print()

# i = input()
# while i:
#     print(i[0:10])
#     i = i[10:]

#2741
# n = int(input())
# for i in range(n):
#     print(i+1)

# print(*range(1,int(input())+1))

#2742
# print(*range(int(input()),0, -1))

#2739
# n = int(input())
# for i in range(1,10,1):
#     print("%d * %d = %d" %(n,i,n*i))

#1924
# date = [31,28,31,30,31,30,31,31,30,31,30,31]
# days = ['SUN','MON','TUE','WED','THR','FRI','SAT']
# x, y = map(int,input().split(' '))
# Day = 0
# for i in range(0, x-1):
#     Day += date[i]

# Day = (Day+y) %7
# print(days[Day])

#8393
# sum = 0
# for i in range(int(input())+1):
#     sum += i

# print(sum)

# n = int(input())
# print(n*-~n//2)

#10818
# n = int(input())
# arr = list(map(int,input().split(" ")))
# print(min(arr),max(arr))

# #2438
# for i in range(1,int(input())+1):
#     print("*" * i)


#2439
# n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i), end="")
#     print("*"*i)

#2440
# for i in range(int(input()),0,-1):
#     print("*"*i)

#2441
# n = int(input())
# for i in range(n,0,-1):
#     print(" "*(n-i), end="")
#     print("*"*i)

#2442
# n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i), end="")
#     print("*"*(2*i-1))

#2445
# n = int(input())
# m = 2
# for i in range(1, n+1):
#     print("*"*i, end="")
#     print(" "*(2*n-2*i), end="")
#     print("*"*i)
# for i in range(n-1,0,-1):
#     print("*"*i, end="")
#     print(" "*m, end="")
#     m += 2
#     print("*"*i)

# x = int(input())
# for i in range(-(x-1), x):
#     print('*' * (x-abs(i)) + ' ' * (abs(i) * 2) + '*' * (x-abs(i)))

#2522
# n = int(input())
# for i in range(-n+1, n):
#     print(' '*abs(i)+'*'*(abs(n)-abs(i)))

