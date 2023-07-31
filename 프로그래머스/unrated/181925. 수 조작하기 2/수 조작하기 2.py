def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1) :
        c = numLog[i+1] - numLog[i]
        if c == 1 :
            answer += 'w'
        elif c == -1 :
            answer += 's'
        elif c == 10 :
            answer += 'd'
        else :
            answer += 'a'
    return answer