def solution(my_string):
    answer = [ my_string[i:] for i in range(len(my_string)-1,-1,-1) ]
    answer = sorted(answer)
    return answer