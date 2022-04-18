# n = int(input())

# arrx = [0,0,-1,1]
# arry = [-1,1,0,0]
# side = ['L','R','U','D']

# x,y = 1,1

# ss = list(input().split())
# for i in ss:
#     if i in side:
       
#         nx = x + arrx[side.index(i)]
#         ny = y +  arry[side.index(i)]
#         if nx>n or nx<1 or ny>n or ny<1:
#            continue
#         x,y = nx, ny
# print(x,y)

# n = int(input())
 
# cnt = 0
# for i in range(n+1): #시
#     for j in range(60): #분
#         for k in range(60): #초
#             if '3' in str(i) + str(j) + str(k):
#                 cnt += 1

# print(cnt)

# inputd = input()
# row = int(inputd[1])
# column = int(ord(inputd[0])) - int(ord('a')) + 1

# steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# result = 0
# for st in steps:
#     nrow = row + st[0]
#     ncol = column + st[1]

#     if nrow >= 1 and nrow <=8 and ncol >= 1 and ncol <= 8:
#         result += 1

# print(result)

n,m = map(int,input().split())

d = [[0] * m for _ in range(n)]

x,y,direction = map(int,input().split())

d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

# 북 동 남 서 
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)