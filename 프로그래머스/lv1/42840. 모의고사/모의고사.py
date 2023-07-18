def solution(answers):
    answer = []
    math_1 = [1,2,3,4,5]
    math_2 = [2,1,2,3,2,4,2,5]
    math_3 = [3,3,1,1,2,2,4,4,5,5]
    nums = [0,0,0]
    idx_1 = 0
    idx_2 = 0
    idx_3 = 0
    for i in range(len(answers)) :
        if answers[i] == math_1[idx_1] :
            nums[0] += 1
        idx_1 += 1
        if idx_1 == len(math_1) :
            idx_1 = 0
        
        if answers[i] == math_2[idx_2] :
            nums[1] += 1
        idx_2 += 1
        if idx_2 == len(math_2) :
            idx_2 = 0    
        
        if answers[i] == math_3[idx_3] :
            nums[2] += 1
        idx_3 += 1
        if idx_3 == len(math_3) :
            idx_3 = 0  
            
    for i in range(3) :
        if nums[i] == max(nums) :
            answer.append(i+1)
    return answer