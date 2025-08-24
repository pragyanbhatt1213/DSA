n=int(input().strip())
magnets=[]
for _ in range(n):
    magnets.append(input().strip())
groups=1
for i in range(n-1):
    if(magnets[i][1]==magnets[i+1][0]):
        groups+=1
print(groups)