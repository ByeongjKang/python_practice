def solution(board, moves):
    stack = []
    count = 0
    for key in moves :
        for layer in board :
            if len(stack) == 0 :
                if layer[key-1] != 0 :
                    stack.append(layer[key-1])
                    layer[key-1] = 0
                    break
            else :
                if layer[key-1] != 0 :
                    if layer[key-1] != stack[-1] :
                        stack.append(layer[key-1])
                        layer[key-1] = 0
                        break
                    else :
                        layer[key-1] = 0
                        stack.pop()
                        count += 2
                        break
    return count
