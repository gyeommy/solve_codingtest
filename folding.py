import math

def solution(wallet, bill):
    answer = 0
    while min(bill) > min(wallet) or max(bill) > max(wallet):
        if bill[0] > bill[1]:
            bill[0] = math.floor(bill[0]/2)
            answer += 1
        else:
            bill[1] = math.floor(bill[1]/2)
            answer += 1
    return answer

wallet = [50,50]
bill = [100,241]

result = solution(wallet, bill)
print(result)

"""
문제에 반복문을 써서, 조건까지 다 주어서 쉽게 풀 수 있었음.
"""