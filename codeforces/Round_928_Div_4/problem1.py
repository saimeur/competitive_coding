t = int(input())
for i in range(t):
    s = input()
    count = 1
    ind = 0
    for j in range(1,len(s)):
        if s[j]==s[0]:
            count+=1
        elif ind ==0:
            ind = j
    if count>=3:
        print(s[0])
    else:
        print(s[ind])