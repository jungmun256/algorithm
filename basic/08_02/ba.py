'''
T = []
a = int(input())
for i in range(a):
    T2 = []
    for j in range(2):
        T2.append(map(int, input().split()))
    T.append(T2)
    print(T2)
print(T)

'''
T = 5
i = 0

for i in range(T):
    a, b = map(int, input().split())
    print(a+b)
