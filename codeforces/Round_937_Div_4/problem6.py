t=int(input())
for i in range(t):
    line= input().split()
    a,b,c = int(line[0]), int(line[1]), int(line[2])
    if a+1 != c :
        print(-1)
    elif a==0:
        print(b)
    else:
        n=-1 #height+1
        a2 = a
        while a2!=0 :
            a2=a2//2
            n+=1
        k = 2**(n+1)-1 -a
        if b<= k:
            print(n+1)
        else:
            b=b-k
            nb = 2**(n+1)-k
            j= b//nb
            if b%nb!=0:
                j+=1
            print(n+j+1)