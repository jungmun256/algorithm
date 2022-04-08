#2751
# n = int(input())
# d = []
# for i in range(n):
#     d.append(int(input()))

# for i in sorted(d):
#     print(i)

#2193
# dp = [0,1,1]

# for i in range(3,91):
#     dp.append(dp[i-2] + dp[i-1])

# n = int(input())
# print(dp[n])

#1912
# n = int(input())
# arr = list(map(int,input().split()))
# dp = [0] * len(arr)
# dp[0] = arr[0]

# for i in range(1,len(arr)):
#     dp[i] = max(arr[i], dp[i-1]+arr[i])

# print(max(dp))

#2579
n = int(input())
dp = [0] * n

for i in range(n):
    dp[i] = int(input())

for i in range(1,n):
    result = result +  max(dp[i], dp[i]+dp[i+1], dp[i]+dp[i+2])

print(result)