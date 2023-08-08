def solution(arr):
    x = len(arr)
    c = bin(x)
    while c.count('1') != 1 :
        arr.append(0)
        x += 1
        c = bin(x)
        
    return arr