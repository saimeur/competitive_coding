t = int(input())
for i in range(t):
    n = int(input())
    sets = [[]]
    for k in range(n):
        s1, s2 = input().split()
        ind=[]
        for j in range(len(sets)):
            if s1 in list(map(lambda x: x[0], sets[j])) or s2 in list(map(lambda x: x[1], sets[j])):
                ind.append(j)
        if ind==[]:
            sets.append([(s1,s2)])
        else:
            sets[ind[0]].append((s1,s2))
        for l in range(1,len(ind)):
            sets[ind[0]]+= sets[ind[l]]
            sets.remove(sets[ind[l]])
    print(n-max(list(map(len, sets))))