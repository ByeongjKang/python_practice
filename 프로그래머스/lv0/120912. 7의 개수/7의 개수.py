def solution(array):
    answer = ''.join( str(x) for x in array )
    return answer.count('7')