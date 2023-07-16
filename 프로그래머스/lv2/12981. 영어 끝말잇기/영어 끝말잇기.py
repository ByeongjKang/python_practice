def solution(n, words):
    answer = [words[0]]
    count = 1
    for key in words[1:] :
        count += 1
        if answer[-1][-1] != key[0] :
            return [(count-1)%n +1, (count-1)//n +1]
        else :
            if key in answer :
                return [(count-1)%n +1, (count-1)//n +1]
            else :
                answer.append(key)
    return [0,0]