def solution(arr, flag):
    X = []
    for a, b in zip(arr, flag) :
        if b :
            X += [a]*(a*2)
        else :
            for i in range(a) :
                X.pop() 
    return X