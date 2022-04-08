# def solution(N, stages):
#     answer = []
#     rates = []
#     player = len(stages)
#     print(stages.count(1))
#     for i in range(N):
#         if player == 0:
#             break
#         rate = stages.count(i+1) / player
#         rates.append(rate)
#         player -= stages.count(i+1)
        
#     rates = list(enumerate(rates))
#     rates = sorted(rates, key=lambda x:x[1], reverse=True)
#     for i in range(len(rates)):
#         answer.append(rates[i][0]+1)
#     return answer

# def solution(N, stages):
#     answer = []
#     rates = []
#     player = len(stages)
#     #print(stages.count(1))
#     for i in range(N):
#         if player == 0:
#             break
#         #rate = stages.count(i+1) / player
#         rates.append(stages.count(i+1) / player)
#         player -= stages.count(i+1)
        
#     rates = list(enumerate(rates))
#     rates = sorted(rates, key=lambda x:x[1], reverse=True)
#     for i in range(len(rates)):
#         answer.append(rates[i][0]+1)
#     return answer

# def solution(N, stages):
#     result = {}
#     denominator = len(stages)
#     for stage in range(1, N+1):
#         if denominator != 0:
#             count = stages.count(stage)
#             result[stage] = count / denominator
#             denominator -= count
#         else:
#             result[stage] = 0
#     return sorted(result, key=lambda x : result[x], reverse=True)

# dartResult = '1S2D*3T'
# n = ''
# score = []
# for i in dartResult:
#     if i.isnumeric():
#         n += i
#     elif i == 'S':
#         n = int(n) ** 1
#         score.append(n)
#         n = ''
#     elif i == 'D':
#         n = int(n) ** 2
#         score.append(n)
#         n = ''
#     elif i == 'T':
#         n = int(n) ** 3
#         score.append(n)
#         n = ''
#     elif i == '*':
#         if len(score) > 1:
#             score[-2] = score[-2] * 2
#             score[-1] = score[-1] * 2
#         else:
#             score[-1] = score[-1] * 2
#     elif i == '#':
#         score[-1] = score[-1] * -1

# print(sum(score))    

# n = 5
# arr1 = [9,20,28,18,11]
# arr2 = [30,1,21,17,28]

# answer = []
# for a1,a2 in zip(arr1,arr2):
#     a12 = str(bin(a1 | a2))[2:]
#     a12 = '0' * (n-len(a12)) + a12
#     a12 = a12.replace('1','#')
#     a12 = a12.replace('0',' ')
#     answer.append(a12)
#     #print(a12)
# print(answer)

# N = 5
# stages = [2,1,2,6,2,4,3,3]
# result = {}
# denominator = len(stages)
# for stage in range(1,N+1):
#     if denominator != 0:
#         cnt = stages.count(stage)
#         result[stage] = cnt / denominator
#         denominator -= cnt
#     else:
#         result[stage] = 0

# print(sorted(result,key=lambda x:result[x],reverse=True))

# s = 'one4seveneight'
# eng = ['zero','one','two','three','four','five','six','seven','eight','nine']
# for i in range(len(eng)):
#     s = s.replace(eng[i],str(i))
# print(s)

# import re
# new_id = '...!@BaT#*..y.abcdefghijklm'
# answer = new_id.lower()
# answer = re.sub('[^a-z0-9\-_.]','',answer)
# answer = re.sub('\.+','.',answer)
# answer = re.sub('^[.]|[.]$','',answer)
# if answer == '':
#     answer = 'a'
# answer = answer[:15]
# answer = re.sub('[.]$','',answer)
# while len(answer)<3:
#     answer += answer[-1]
# print(answer)


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

answer = [0] * len(id_list)
dict_list = {i:[] for i in id_list}
for i in set(report):
    i = i.split(' ')
    dict_list[i[1]].append(i[0])

for key,value in dict_list.items():
    if len(value) >= k:
        for v in value:
            print(v)
            answer[id_list.index(v)] += 1

print(answer)