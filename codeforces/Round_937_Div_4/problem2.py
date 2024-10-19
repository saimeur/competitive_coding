t = int(input())
for i in range(t):
    n = int(input())
    for j in range(2*n):
        if j%4 < 2 :
            print(n//2 * "##.." + (n%2)*"##")
        else :
            print(n//2 * "..##" + (n%2)*"..")
