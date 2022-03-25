# # 기능 개발
# def solution(progresses, speeds):
#     answer = []
#     days = 0
#     cnt = 0

#     while len(progresses) != 0:
#         if progresses[0] + speeds[0]*days >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             cnt += 1
#         else:
#             if cnt > 0:
#                 answer.append(cnt)
#                 cnt = 0
#             days += 1
#     answer.append(cnt)
#     return answer
# solution([93, 30, 55],[1,30,5])

# # 프린터
# def solution(priorities, location):
#     printer = [(i,p) for i,p in enumerate(priorities)]

#     turn = 0

#     while printer:
#         job = printer.pop(0)
#         if any(job[1] < other_job[1] for other_job in printer):
#             printer.append(job)
#         else:
#             turn += 1
#             if job[0] == location:
#                 break
#     return turn

# # 다리를 지나는 트럭
# def solution(bridge_length, weight, truck_weights):
#     time = 0
#     q = [0] * bridge_length
#     while q:
#         time += 1
#         q.pop(0)

#         if truck_weights:
#             if sum(q) + truck_weights[0] <= weight:
#                 q.append(truck_weights.pop(0))
#             else:
#                 q.append(0)
#     return time


# --------------------------------------
# def solution(numbers, target):
#     answer = 0
#     leaves = [0]
#     for num in numbers:
#         tmp = []
#         print('num = ',num,end=' ')
#         for parent in leaves:
#             print('parent = ',parent)
#             tmp.append(parent + num)
#             tmp.append(parent - num)
#         leaves = tmp
#     for leaf in leaves:
#         if leaf == target:
#             answer += 1
#     return answer

# print(solution([1, 1, 1, 1, 1],3))

# ---------------------------------------
from itertools import product

def solution(numbers,target):
    l = [(x,-x) for x in numbers]
    print(l)
    s = list(map(sum, product(*l)))
    return s.count(target)


print(solution([4,1,2,1],4))
