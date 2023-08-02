def solution(order):
    cnt = 0
    for key in str(order) :
        if key == '3' or key == '6' or key == '9' :
            cnt += 1
    return cnt