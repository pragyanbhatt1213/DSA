n=int(input())
p=list(map(int,input().split()))
result=[0]*n  
for giv in range(n):
    rec = p[giv]
    result[rec - 1] = giv + 1 # Friend `giv+1` gave to friend `rec`
print(*result)