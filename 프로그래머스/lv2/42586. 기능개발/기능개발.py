from math import ceil

def solution(progresses, speeds):
    time = []
    for i in range(len(progresses)) :
        time.append((100-progresses[i])/speeds[i])
    
    answer = []
    count = 1
    localmax = time[0]
    for j in range(0, len(time)-1) :
        
        if ceil(localmax) < ceil(time[j+1]) :
            answer.append(count)
            localmax = time[j+1]
            count = 1
        else :
            count += 1
        if j == len(time)-2 :
            answer.append(count)
        
    return answer