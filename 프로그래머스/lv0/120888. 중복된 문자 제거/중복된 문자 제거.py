def solution(my_string):
    alpha_dict = {}
    answer = ''
    for key in my_string :
        if key not in alpha_dict :
            alpha_dict[key] = 1
            answer += key
    return answer