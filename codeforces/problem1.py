t = int(input())
for i in range(t):
    line = input().split(' ')
    a,b,c = line
    a=int(a)
    b=int(b)
    c=int(c)
    if a<b<c :
        print('STAIR')
    elif a<b>c: 
        print('PEAK')
    else: 
        print("NONE")