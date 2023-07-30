def solution(strArr):
    answer = []
    for key in strArr :
        if 'ad' not in key :
            answer.append(key)
    return answer