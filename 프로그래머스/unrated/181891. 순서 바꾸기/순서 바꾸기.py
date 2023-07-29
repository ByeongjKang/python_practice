def solution(num_list, n):
    queue = num_list 
    for i in range(n) :
        queue = queue[1:] + queue[:1]
    return queue