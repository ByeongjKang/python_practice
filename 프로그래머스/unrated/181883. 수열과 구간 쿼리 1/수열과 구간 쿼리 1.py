def solution(arr, queries):
    answer = []
    for x in queries :
        a, b = x[0], x[1] 
        for y in range(a,b+1) :
            arr[y] += 1
    return arr