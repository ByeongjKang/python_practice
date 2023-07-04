def solution(n, arr1, arr2):
    wall = ['']*n
    for i in range(n) :
        for j in range(n) :
            if arr1[i]%2 == 1 or arr2[i]%2 ==1 :
                wall[i] += '#'
                
            else : 
                wall[i] += ' '
            arr1[i] = arr1[i]//2
            arr2[i] = arr2[i]//2
    return [ x[::-1] for x in wall ]
