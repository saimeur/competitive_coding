def carre(n):
    for i in range(n):
        if i%2 == 0:
            res=''
            for k in range(n):
                if k%2==0:
                    res+=2*'#'
                else:
                    res+=2*'.'
            print(res)
            print(res)
        else:
            res=''
            for k in range(n):
                if k%2==0:
                    res+=2*'.'
                else:
                    res+=2*'#'
            print(res)
            print(res)

t = int(input())
for i in range(t):
    n = int(input())
    carre(n)
