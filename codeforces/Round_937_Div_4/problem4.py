l=[]
for i in range(32):
    n = int(bin(i)[2:])
    l.append(n)
l.append(100000)

t = int(input())
for i in range(t):
    n = int(input())
    if n in l:
        print("YES")
    else:
        res = "NO"
        for d in l :
            if d > 1 :
                while n%d==0 :
                    n = n//d 
        if n in l :
            res = "YES"
        print(res)
