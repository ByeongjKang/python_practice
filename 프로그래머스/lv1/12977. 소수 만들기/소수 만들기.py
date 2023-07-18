import itertools

def solution(nums):
    combi = list(itertools.combinations(nums,3))
    sumlist = [sum(combi[i]) for i in range(len(combi))]
    maximum = max(sumlist)
    prime = [x for x in range(2,maximum+1)]
    for i in range(2,maximum) :
        k = 2
        while i*k <= maximum :
            if i*k in prime :
                prime.remove(i*k)
            k += 1
            
    count = 0
    for key in sumlist :
        if key in prime :
            count += 1
    
    return count