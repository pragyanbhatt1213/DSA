n=int(input())
heights=list(map(int, input().split()))
count=0
for i in range(n):
    curr=1  
    j=i-1
    while j>=0 and heights[j]<=heights[j+1]:
        curr+=1
        j-=1
    j=i+1
    while j<n and heights[j]<=heights[j-1]:
        curr+=1
        j+=1
    count=max(count,curr)
print(count)
