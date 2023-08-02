def solution(arr, intervals):
    answer = []
    for key in intervals :
        answer.extend(arr[key[0]:key[1]+1])
    return answer