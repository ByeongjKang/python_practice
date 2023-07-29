def solution(num_str):
    l = list(num_str)
    c = 0
    for key in l :
        c += int(key)
    return c