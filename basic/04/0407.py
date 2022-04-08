# def solution(record):
#     answer = []
#     namespace = {}
#     printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
#     for r in record:
#         rr = r.split(' ')
#         if rr[0] in ['Enter', 'Change']:
#             namespace[rr[1]] = rr[2]

#     for r in record:
#         if r.split(' ')[0] != 'Change':
#             answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

#     return answer

# def solution(record):
#     answer = []
#     userDB = dict()
#     actions = []
 
#     for event in record:
#         info = event.split()
#         action, userid = info[0], info[1]
#         if action in ("Enter","Change"):
#             #nickname = info[2]
#             userDB[userid] = info[2]
#         actions.append((action,userid))
#     print('userDB',userDB)
#     print('actions',actions)
#     for actionInfo in actions:
#         action,userid = actionInfo[0], actionInfo[1]
#         if action == 'Enter':
#              answer.append(f'{userDB[userid]}님이 들어왔습니다.')
#         elif action == 'Leave':
#              answer.append(f'{userDB[userid]}님이 나갔습니다.')
#     #print(actions)
#     return answer

def solution(s):
    result = []
    if len(s) == 1:
        return 1
    for i in range(1,(len(s)//2)+1): #최대 길이가 반
        b = ''  # 매번 쪼갰을 때나오는 문자열 저장, 매번 초기화
        cnt = 1 # 문자열이 연속적으로 반복되는지 체크
        tmp = s[:i] # 첫번째 인덱스에 있는 문자 
        #print('tmp=',tmp,'i=',i)
        #print('i=',i)
        for j in range(i,len(s),i):
            #print('j=',j,'s[j:i+j]=',s[j:i+j])
             
            if tmp == s[j:i+j]:
                cnt+=1
            else:
                if cnt != 1:
                    b = b + str(cnt) + tmp
                else:
                    b = b+tmp
                tmp = s[j:j+i]
                cnt = 1
             
        if cnt != 1:
            b = b+str(cnt) + tmp
        else:
            b = b+tmp
        
        result.append(len(b))
           
    return print(min(result))


solution('aabbaccc')