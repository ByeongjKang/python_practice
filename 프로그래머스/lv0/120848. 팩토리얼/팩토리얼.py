def solution(n):
    x = 1
    cnt = 0
    if n == 1 :
        return 1
    while n >x :
        cnt += 1
        x = x*cnt
        if x > n :
            return cnt - 1
        
    return cnt