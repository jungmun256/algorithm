# 퀵정렬
# array = [5,7,9,0,3,1,6,2,4,8]

# def quick_sort(array,start,end):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end
#     while left <= right:
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
#         if left > right:
#             array[right], array[pivot] = array[pivot], array[right]
#         else:
#             array[left], array[right] = array[right], array[left]

#     quick_sort(array,start,right-1)
#     quick_sort(array,right+1, end)

# quick_sort(array,0,len(array)-1)
# print(array)

# array = [5,7,9,0,3,1,6,2,4,8]

# def quick_sort(array):
#     if len(array) <= 1 :
#         return array

#     pivot = array[0]
#     tail = array[1:]

#     left_side = [x for x in tail if x <= pivot]
#     right_side = [x for x in tail if x>=pivot]

#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# print(quick_sort(array))

# ------------------------------------------------

# 계수 정렬
# array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# count = [0] * (max(array)+1)

# for i in range(len(array)):
#     count[array[i]] += 1

# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i,end=" ")

# ------------------------------------------------

# key
# array = [('바나나',2),('사과',5),('당근',3)]

# def setting(data):
#     print(data[1])
#     return data[1]

# result = sorted(array, key=setting)
# print(result)

# ------------------------------------------------

# p178 위에서 아래로
# n = int(input())
# s = []
# for i in range(n):
#     s.append(int(input()))
# # s.sort()
# # s.reverse()
# # print(s)
# s = sorted(s, reverse=True)

# for i in s:
#     print(i,end=" ")

# ------------------------------------------------

# p180 성적이 낮은 순서대로 학생 출력하기
# n = int(input())
# student = []

# # 함수 이용시
# # def setting(data):
# #     return(data[1])

# for i in range(n):
#     # s.append(input().split()) -> 점수 int형으로 변환X
#     data = input().split()

#     student.append((data[0],int(data[1])))

# student = sorted(student, key=lambda student:student[1])

# # student = sorted(student, key=setting)

# for i in student:
#     print(i[0],end=' ')

# ------------------------------------------------

# p182 두 배열의 원소 교체 방법1
# n, k = map(int,input().split())

# a = list(map(int,input().split()))
# b = list(map(int,input().split()))

# a.sort()
# b.sort()

# # print(a)
# # print(b)

# for i in range(k):
#     a[i],b[-i] = b[-i],a[i]

# print(sum(a))
# # print(b)


# p182 두 배열의 원소 교체 방법2
# n, k = map(int,input().split())

# a = list(map(int,input().split()))
# b = list(map(int,input().split()))

# a.sort()
# b.sort(reverse=True)

# for i in range(k):
#     if a[i] < b[i]:
#         a[i], b[i] = b[i],a[i]
#     else:
#         break
# print(sum(a))

# ------------------------------------------------

# 순차 탐색 소스코드
# def sequential_search(n, target, array):
#     for i in range(n):
#         if array[i] == target:
#             return i+1

# print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요")
# input_data = input().split()
# n = int(input_data[0])
# target = input_data[1]

# print("앞서 적은 원소 개수만큼 문자열을 입력하세요 구분은 띄어쓰기 한 칸으로 합니다.")
# array = input().split()
# # print(array) -> ['Hanul', 'Jonggu', 'Dongbin', 'Taeil', 'Sangwook']

# print(sequential_search(n,target,array))

# ------------------------------------------------

# 재귀 함수를 구현한 이진 탐색 소스코드
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else : 
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else : 
    print(result +1 )