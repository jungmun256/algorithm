# 1463
# x = int(input())
# d = [0] * (x+1)

# for i in range(2,x+1):
#     d[i] = d[i-1]+1
#     if i % 3 == 0:
#         d[i] = min(d[i],d[i//3] + 1)
#     if i % 2 == 0:
#         d[i] = min(d[i],d[i//2] +1 )
# print(d[x])

#11726
# n = int(input())

# def tile(n):
#     d = [0] * 1001
#     d[0] = 0
#     d[1] = 1
#     d[2] = 2

#     for i in range(3,1001):
#         d[i] = d[i-2] + d[i-1]
#     return d[n] % 10007

# print(tile(n))

#9095
# dp = [0 for _ in range(11)]
# def init_dp():
#     dp[1] = 1
#     dp[2] = 2
#     dp[3] = 4
#     for i in range(4,11):
#         dp[i] = dp[i-3]+dp[i-2]+dp[i-1]

# init_dp()
# T = int(input())
# for t in range(T):
#     n = int(input())
#     print(dp[n])