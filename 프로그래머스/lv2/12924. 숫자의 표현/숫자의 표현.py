def solution(n):
    result = 0
    if n == 1 :
        return 1
    for a in range(1, n) :
        s = (a-1)*a//2
        if n-s <= 0 :
            break
        if (n-s)%a == 0 : 
            result += 1
    
        
    return result
