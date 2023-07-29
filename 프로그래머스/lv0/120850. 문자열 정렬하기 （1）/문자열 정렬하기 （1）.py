def solution(my_string):
    answer = []
    for key in my_string :
        if key.isdigit() :
            answer.append(int(key))
    answer = sorted(answer)
    return answer