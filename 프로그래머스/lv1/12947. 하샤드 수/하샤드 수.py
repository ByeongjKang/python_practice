def solution(x):
    num_list = []
    t = x 
    while True :
        num_list.append(t%10)
        if t//10 == 0 :
            break
        t = t//10
    return x % sum(num_list) == 0