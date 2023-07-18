def solution(k, score):
    result = []

    for i in range(1, len(score)+1) :
        temp = score[0:i]
        temp.sort(reverse=True)
        if i < k+1 : 
            result.append(temp[-1])
        else :
            result.append(temp[k-1])
    return result


"""def solution(k, score):
    if len(score) < k :
        result = [ min(score[:i]) for i in range(1,len(score)+1) ]
        return result
    result = [ min(score[:i]) for i in range(1, k+1)]
    temp = score[:k]
    for j in range(k,len(score)) :
        temp.append(score[j])
        temp.remove(min(temp))
        result.append(min(temp))
    return result"""