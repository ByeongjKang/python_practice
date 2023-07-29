def solution(arr, idx):
    for a, b in enumerate(arr) :
        if b == 1 and a >= idx :
            return a
    return -1