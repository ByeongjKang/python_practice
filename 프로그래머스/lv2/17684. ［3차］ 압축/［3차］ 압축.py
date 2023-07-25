def solution(msg):
    alphabet_list = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P': 16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26 }
    i = 0
    answer_idx = []
    while i < len(msg) :
        key = ''
        for j in range(i, len(msg)) :
            key += msg[j]
            i += 1
            if key not in alphabet_list :
                alphabet_list[key] = len(alphabet_list)+1
                answer_idx.append(alphabet_list[key[:-1]])
                i = j
                break
            if j == len(msg)-1 :
                answer_idx.append(alphabet_list[key])
    return answer_idx