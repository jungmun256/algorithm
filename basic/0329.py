# 그리디 - 거스름돈
# n = 1260
# count = 0

# coin_types = [500,100,50,10]

# for coin in coin_types:
#     count += n // coin
#     n %= coin

# print(count)

# ------------------------------

# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()

# first = data[n-1]
# second = data[n-2]

# result = 0

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1

# print(result)




# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()

# first = data[n-1]
# second = data[n-2]

# count = int(m / (k+1)) * k
# count += m % (k+1)

# result = 0
# result += (count) * first
# result += (m-count) * second

# print(result)


# n, m = map(int, input().split())
# result = []
# for i in range(n):
#     data = list(map(int, input().split()))
#     result.append(min(data))

# print(max(result))



# n, k = map(int, input().split())
# result = 0

# while n >= k:
#     while n % k != 0:
#         n -= 1
#         result += 1
#     n // k
#     result += 1

# while n > 1:
#     n -= 1
#     result += 1

# print(result)

