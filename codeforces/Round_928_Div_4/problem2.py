t = int(input())
for t1 in range(t):
    n= int(input())
    for i in range(n):
        line = input()
        start = -1; end =-1; mid =-1
        for j in range(n):
            if line[j]==1 :
                if start == -1:
                    start = j
                else:
                    end = j
            if line[j]==0 and start != -1:
                break
        if (end-start+1)%2 ==0:
            print("SQUARE")