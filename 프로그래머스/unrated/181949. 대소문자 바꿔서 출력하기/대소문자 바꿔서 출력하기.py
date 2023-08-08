str = input()
answer = ''
for k in str :
    if k.isupper() :
        answer += k.lower()
    else :
        answer += k.upper()
print(answer)