def solution(s):
    answer = ''
    string_list = list(map(str, s.split()))
    for key in string_list :
        for i in range(len(key)) :
            if i%2 == 0 :
                answer += key[i].upper()
            else :
                answer += key[i].lower()
    answer2 = ''
    idx = 0
    for char in s :
        if char == ' ' :
            answer2 += ' '
        else :
            answer2 += answer[idx]
            idx += 1
    return answer2
