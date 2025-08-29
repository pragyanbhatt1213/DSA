import math
def prime(x):
    if x<2:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
n, m = map(int,input().split())
next_prime=-1
for i in range(n+1,51):   
    if prime(i):
        next_prime=i
        break
if next_prime==m:
    print("YES")
else:
    print("NO")
