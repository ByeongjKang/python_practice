def solution(N, stages):
    failure_rate = []

    s = len(stages)
    for i in range(1, N+1) :
        c = stages.count(i)
        if c == 0 :
            failure_rate.append(0)
        else :
            failure_rate.append(c/s)
            s -= c


    answer = []
    for j in range(N) :
        maximum = max(failure_rate)
        answer.append(failure_rate.index(maximum)+1)
        failure_rate[failure_rate.index(maximum)] = -1
     

    return answer