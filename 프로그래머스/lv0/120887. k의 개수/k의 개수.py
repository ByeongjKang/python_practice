def solution(i, j, k):
    series = ''
    for x in range(i,j+1) :
        series += str(x)
    return series.count(str(k))