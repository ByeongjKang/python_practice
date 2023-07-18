def solution(k, score):
    if len(score) < k :
        result = [ min(score[:i]) for i in range(1,len(score)+1) ]
        return result
    result = [ min(score[:i]) for i in range(1, k+1)]
    temp = score[:k]

    for j in range(k,len(score)) :
        temp.append(score[j])
        temp.remove(min(temp))
        result.append(min(temp))
    return result