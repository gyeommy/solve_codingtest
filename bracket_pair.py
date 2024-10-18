# def solution(s):
#     answer = True
    
#     while len(s) > 0:
#         if s.count('(') == s.count(')') and s.endswith(')'):
#             if s.startswith('('):
#                 s = s[1:len(s)-1]
#                 if len(s) == 0:
#                     answer = True
#                     return answer
#         else:
#             answer = False
#             return answer

#     return answer

# s = "()()"
# result = solution(s)

# print(result)

# s = "()()"
# print(len(s))
# s = s[1:len(s)-1]
# print(s)

"""
문자열 s 괄호 '(' ')' 로만 구성

1. 문자열 s가 끝날때 ) 로 끝나야함
2. '(' ,' )'  갯수가 짝을 이루어야 함

두가지 조건을 모두 만족해야 함

len(s) % 2 = 0

s.endswith(')')
→ 반례
s= "))))" 이면  True로 인식하게됨
count()로 세어서 같은 갯수일때로 변경

s.count('() == s.count(')')

반례: ( ) ) ( ( )
→ s문자열에서 
')' 로 끝나는 경우 제일 먼저 '(' 를 같이 제거한다.
맨 앞의 '(' 와 맨 뒤의 ')' 를 제거한 문자열에 똑같은 작업을 반복한다.

→위와 같이 접근 했으나

처음 시작한 접근이 완전 틀렸다.
끝과 시작을 확인해 양끝부터 ()를 각각 제거하려했는데 이렇게 하면
괄호의 시작과 끝이 서로 매칭되지 않으면 False를 반환하게 되어 반례가 생긴다.
"""

def solution(s):
    answer = True
    arr = []
    for i in s:
        if i == '(':
            arr.append(i)
        else:
            if len(arr)==0:
                answer = False
            else:
                arr.pop()

    if len(arr) > 0:
        answer = False
    
    return answer