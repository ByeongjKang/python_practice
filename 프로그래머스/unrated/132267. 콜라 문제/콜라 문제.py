def solution(a, b, n):
    answer = 0
    while n >= a :
        q = n//a
        r = n%a
        answer += q * b
        n = q*b + r
    return answer