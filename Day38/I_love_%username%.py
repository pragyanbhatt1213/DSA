n=int(input())
points=list(map(int, input().split()))  
count=0
worst=points[0]
best=points[0]
for i in range(1,n):
    if(points[i]>best):
        best=points[i]
        count+=1
    elif(points[i]<worst):
        worst=points[i]
        count+=1
print(count)