def compare(s1,s2):
    ans= 0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            ans+=1
    return ans<=1

def find_divisors(n):
    divisors = []
    # Iterate from 1 to square root of n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            # If i is a divisor, add it to the list
            divisors.append(i)
            # If i is not the square root of n, add n/i as well
            if i != n // i:
                divisors.append(n // i)
    return divisors

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    div = find_divisors(n)
    div.sort()
    for d in div:
        x1 = s[:d]
        x2 = s[-d:]
        if compare(x1*(n//d), s) or compare(x2*(n//d), s):
            print(d)
            break
            
            