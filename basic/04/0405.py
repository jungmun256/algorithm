# def solution(id_list, report, k):
    
#     # 딕셔너리 생성
#     dic_report = {id:[] for id in id_list}
#     # print(dic_report)
#     answer = [0] * len(id_list)
#     for re in set(report):
#         re = re.split(' ')
#         dic_report[re[1]].append(re[0])
#     #print(dic_report)

#     #print(dic_report)
#     # {'muzi': ['apeach'], 'frodo': ['apeach', 'muzi'], 'apeach': [], 'neo': ['muzi', 'frodo']}
#     # dict_items([('muzi', ['apeach']), ('frodo', ['apeach', 'muzi']), ('apeach', []), ('neo', ['frodo', 'muzi'])])
#     # items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다


#     for key, value in dic_report.items():
#        if len(value) >= k:
#             for v in value:
#                 answer[id_list.index(v)] += 1
#     return answer


def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        #if c.isalpha() or c.isdigit() or c in "-_.":
        if c.isalnum() or c in "-_.":
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer and answer[0] == '.':
    # if answer[0:1] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
    # if answer[-1:0] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    print(answer)
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer