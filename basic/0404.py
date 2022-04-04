# # 부품 찾기 (이진탐색)
# n = int(input())
# data = list(map(int,input().split()))

# m = int(input())
# find = list(map(int,input().split()))

# for i in find:
#     if i in data:
#         print('yes')
#     else:
#         print('no')

# n,m = map(int,input().split())

# data = list(map(int,input().split()))

# start = 0
# end = max(data)
# data.sort()

# result = 0
# while (start <= end):
#     sum = 0
#     mid = (start + end) // 2

#     for i in data:
#         if i > mid:
#             sum += i - mid
        
        
#     if sum < m:
#         end = mid -1
#     else:
#         result = mid
#         start = mid + 1

# print(result)



# n = int(input())
# data = list(map(int,input().split()))

# sum1,sum2 = 0,0

# for i in range(0,n,2):
#     sum1 += data[i]
# for i in range(1,n,2):
#     sum2 += data[i]

# print(max(sum1,sum2))


n,m = map(int,input().split())
data = []
for i in range(n):
    data.append(int(input()))

