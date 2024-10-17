def solution(n,m):
    answer = []
    num1 = max(n,m)    
    num2 = min(n,m)    
    gcd=1
    lcm=1
    for i in range(1, num1):
        a = n%i
        b = m%i
        if a == 0 and b == 0:
            if i != 1:
                gcd = i
            else:
                gcd = i
    
    lcm = int(num1*num2/gcd)
    answer = [gcd,lcm]
    return answer