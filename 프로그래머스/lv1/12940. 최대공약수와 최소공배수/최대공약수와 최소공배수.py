def solution(n, m):
    answer = []
    minimum = min(n,m)
    maximum = max(n,m)
    for i in range(minimum,0,-1) :
        if n%i == 0 and m%i == 0 :
            answer.append(i)
            break
    answer.append(answer[0]*(n/answer[0])*(m/answer[0]))
    return answer


