def solution(rsp):
    answer = ''
    for key in rsp :
        if key == '2' :
            answer += '0'
        elif key == '5' :
            answer += '2'
        else :
            answer += '5'
    return answer
