# --------------------------------------------------------

# 완주하지 못한 선수

# 풀이 1
# def solution(participant, completion):
#     answer = 0
#     hashdire = {}
#     for part in participant:
#         hashdire[hash(part)] = part
#         answer += hash(part)
#     for com in completion:
#         answer -= hash(com)
        
#     return hashdire[answer]


# 풀이 2
# import collections

# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     print(answer)
#     print(answer.keys())
#     print(list(answer.keys()))
#     return list(answer.keys())[0]

# 풀이 3
# import collections

# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     # print(list(answer.keys())[0])
#     # 딕셔너리 값에서 키 값만 출려 하고 싶을 때 
#     # .keys() -> list() -> [0]
#     return list(answer.keys())[0]


# --------------------------------------------------------

# 전화번호 목록
# def solution(phone_book):
#     phone_book.sort()
    
#     answer = True
#     for p1,p2 in zip(phone_book, phone_book[1:]):  # zip 사용 **
        
#         if p2.startswith(p1):
#             answer = False
#     return answer

# --------------------------------------------------------

# 위장

# 1
# def solution(clothes):
#     answer = 1
#     hash_map = {}
#     for clothe,type in clothes:
#         hash_map[type] = hash_map.get(type,0) +1
#     print(hash_map)
#     for type in hash_map:
#         print(hash_map[type])
#         answer *= (hash_map[type] + 1)
#     return answer-1

# 2
# def solution(clothes):
#     answer = 1
#     hmap = {}
#     # for cloth in clothes:
#     #     print(cloth)  -> ['yellow_hat', 'headgear']
#     # for cloth,type in clothes:
#     #     print(cloth,type) -> yellow_hat headgear
#     for cloth,type in clothes:
#         # 타입의 value값을 가지고 오는데 존재 하지 않는다면 초기값을 0으로 
#         hmap[type] = hmap.get(type,0) + 1
        
#     # print(hmap) -> {'headgear': 2, 'eyewear': 1}
#     for i in hmap:
#         # print(hmap[i]) -> 2 1 
#         answer *= (hmap[i] + 1)
#     return answer-1

#3
# import collections

# def solution(clothes):
#     answer = 1
#     count = collections.Counter(type for cloth,type in clothes)
#     # print(list(count.values())[0])
#     for i in count:
#         answer *= (count[i] + 1)
#     return answer-1


# 4
import collections
from functools import reduce
def solution(clothes):
    
    count = collections.Counter([type for cloth,type in clothes])
    
    answer = reduce(lambda acc,cur:acc*(cur+1),count.values(),1)
    
    return answer-1

# --------------------------------------------------------

# 정렬

# k번째 수
def solution(array, commands):

    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]

# --------------------------------------------------------

# 가장 큰 수

def solution(numbers):
    numbers = list(map(str,numbers))
    # print(numbers)
    numbers.sort(key=lambda x : x*3, reverse=True)
    # print(numbers)
    return str(int(''.join(numbers)))


# --------------------------------------------------------

# 완전 탐색
# 모의고사
# def solution(answers):
#     answer = []
#     a1 = [1,2,3,4,5]
#     a2 = [2,1,2,3,2,4,2,5]
#     a3 = [3,3,1,1,2,2,4,4,5,5]
#     s = [0,0,0]
    
#     for idx,num in enumerate(answers):
               
#         if a1[idx%len(a1)] == num:
#             s[0] += 1
#         if a2[idx%len(a2)] == num:
#             s[1] += 1
#         if a3[idx%len(a3)] == num:
#             s[2] += 1
    
#     for idx, num in enumerate(s):
#         if num == max(s):
#             answer.append(idx+1)
    
# #     k = max(s)
    
# #     if k == s[0]:
# #         answer.append(1)
# #     if k == s[1]:
# #         answer.append(2)
# #     if k == s[2]:
# #         answer.append(3)
        
#     return answer


# 다시 풀기
# def solution(answers):
#     answer = []
#     p1 = [1,2,3,4,5]
#     p2 = [2,1,2,3,2,4,2,5]
#     p3 = [3,3,1,1,2,2,4,4,5,5]
#     s = [0,0,0]
    
#     for idx,socre in enumerate(answers):
#         if socre == p1[idx%5]:
#             s[0] += 1
#         if socre == p2[idx%8]:
#             s[1] += 1
#         if socre == p3[idx%10]:
#             s[2] += 1
#     print(s)
    
#     for idx,num in enumerate(s):
#         if num == max(s):
#             answer.append(idx+1)
    
#     return answer

# --------------------------------------------------------
