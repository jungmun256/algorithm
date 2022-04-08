# 반복문으로 구현한 이진 탐색 소스 코드
# def binary_search(array,target,start,end):
#     while start <= end:
#         mid = (start+end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

# n, target = list(map(int, input().split()))
# array = list(map(int,input().split()))

# result = binary_search(array, target, 0, n-1)

# if result == None:
#     print("원소가 존재하지 않습니다.")
# else:
#     print(result+1)

# --------------------------------------------------

# 한 줄 입력 받아 출력하는 소스코드
# import sys
# input_data = sys.stdin.readline().rstrip()

# print(input_data)

# --------------------------------------------------

# 부품 찾기

# 집합 자료형 이용
# import sys

# n = int(input())
# product = list(map(int,input().split()))

# m = int(input())
# order = list(map(int,input().split()))

# for i in order:
#     if i in product:    ***
#         print('yes',end=" ")
#     else:
#         print('no',end=" ")

# 계수 정렬 이용
# n = int(input())
# array = [0] * 100001

# for i in input().split():       #가게에 있는 전체 부품 번호를 입력받아서 기록
#     array[int(i)] = 1

# m = int(input())
# x = list(map(int,input().split()))

# for i in x:
#     if array[i] == 1:
#         print('yes',end=" ")
#     else:
#         print('no',end=" ")

# 이진 탐색 소스 코드 구현(반복문)
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start+end) //2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid -1
#         else:
#             start = mid+1
#     return None

# n = int(input())
# array = list(map(int,input().split()))
# array.sort()

# m = int(input())
# x = list(map(int,input().split()))


# for i in x:
#     result = binary_search(array,i, 0, n-1)
#     if result != None:
#         print('yes',end=" ")
#     else:
#         print('no',end=" ")


# --------------------------------------------------


# 떡볶이 떡 만들기

# n, m = map(int,input().split())

# rice = list(map(int,input().split()))

# start = 0
# end = max(rice)

# result = 0
# while start <= end:
#     total = 0
#     mid = (start+end)//2
#     for x in rice:
#         if x > mid :
#             total += x - mid
#     if total < m:
#         end = mid -1
#     else:
#         result = mid
#         start = mid + 1

# print(result)

# --------------------------------------------------

# 피보나치 수열
# d = [0] * 1000

# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:
#         return d[x]
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]

# print(fibo(99))

# d = [0] * 100

# def pibo(x):
#     print('f('+ str(x)+')', end=" ")
    
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:
#         return d[x]

#     d[x] = pibo(x-1) + pibo(x-2)
#     return d[x]

# pibo(6)


# e = [0]*100
# e[1] = 1
# e[2] = 1
# n = 99

# for i in range(3, n+1):
#     e[i] = e[i-1]+e[i-2]
# print(e[n])


# --------------------------------------------------


# x = int(input())
# cnt = 0

# while x == 1:
#     if x % 5 == 0:
#         x /= 5
#         cnt += 1
#     elif x % 5 != 0:
#         x -= 1
#         cnt += 1
#     elif x % 3 == 0:
#         x /= 3
    
#         cnt += 1
#     elif x % 2 == 0:
#         x /= 5
#         cnt += 1
    
    

# print(cnt)



# --------------------------------------------------




# n, m = map(int, input().split())
# cake = list(map(int, input().split()))
# start = 0
# end = max(cake)

# result = 0
# while (start <= end):
#     total = 0
#     mid = (start+end) //2
#     for x in cake:
#         if x > mid : 
#             total += x - mid
    
#     if total < m:
#         end = mid -1
#     else : 
#         result = mid
#         start = mid + 1

# print(result)


# --------------------------------------------------

n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])