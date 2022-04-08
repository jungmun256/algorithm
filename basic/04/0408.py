def solution(left, right):
    answer = 0
    cnt = 0
    for i in range(left,right+1,1):
        for j in i:
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
        cnt = 0
    return answer