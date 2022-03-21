#11720
# n = int(input())
# nums = input()
# total = 0
# for i in range(n):
#     total += int(nums[i])

# print(total)

#11721
# n = input()
# c = 0
# for i in n:
#     print(i,end="")
#     c += 1
#     if(c == 10):
#         print()

#11721
# n = input()
# for i in range(len(n)):
#     print(n[i],end="")
#     if(i % 10 == 9):
#         print()

#2741
# n = int(input())
# for i in range(n):
#     i += 1
#     print(i)


#2742
# n = int(input())
# for i in range(n):
#     print(n-i)


#2739
# n = int(input())
# for i in range(9):
#     i += 1
#     print('%d * %d = %d' %(n,i,n*i))

#8393
# n = int(input())
# sum = 0
# for i in range(1,n+1,1):
#     sum += i
# print(sum)

#10818
n = int(input())
a = input()
c = []
for i in range(n):
    c.append(a.split())

print(c)