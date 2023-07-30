def solution(n):
    answer = []
    for x in range(1, int(n**0.5)+1 ) :
        if n%x == 0 :
            answer.append(x)
            if n//x != x :
                answer.append(n//x)
    answer.sort()
    return  answer