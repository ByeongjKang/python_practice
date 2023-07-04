def solution(k, m, score):
    if len(score) < m :
        return 0
    
    summation = 0
    score.sort(reverse=True)
    for i in range(0,len(score),m) :
        if len(score) >= i+m :
            summation += min(score[i:i+m]) * m
        else :
            break
    return summation
        
    