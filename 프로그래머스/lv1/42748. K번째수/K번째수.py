def solution(array, commands):
    answer = []
    for i in range(len(commands)) :
        temp = array[commands[i][0]-1:commands[i][1]]
        for j in range(len(temp)-1) :
            for k in range(len(temp)-j-1) :
                if temp[k] > temp[k+1] :
                    temp[k], temp[k+1] = temp[k+1], temp[k]
        answer.append(temp[commands[i][2]-1])
    return answer