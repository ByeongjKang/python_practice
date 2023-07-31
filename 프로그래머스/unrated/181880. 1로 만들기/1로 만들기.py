def solution(num_list):
    result = 0
    for key in num_list :
        cnt = 0
        while key > 1 :
            cnt += 1
            if key%2 == 0 :
                key = key//2
            else :
                key = (key-1)//2
        result += cnt
    return result