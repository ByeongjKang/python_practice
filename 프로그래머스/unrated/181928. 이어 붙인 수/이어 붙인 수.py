def solution(num_list):
    even = ''
    odd = ''
    for key in num_list :
        if key%2 == 1:
            odd += str(key)
        else :
            even += str(key)
    return int(odd)+int(even)