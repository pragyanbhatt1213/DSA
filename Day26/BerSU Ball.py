n=int(input())
boys=list(map(int, input().split()))
m=int(input())
girls=list(map(int, input().split()))
boys.sort()
girls.sort()
pair=0
b=0
g=0
while(b<n and g<m):
    if(abs(boys[b]-girls[g])<=1):
        pair+=1
        b+=1
        g+=1
    elif(boys[b]>girls[g]):#girls level is too low (as sorted list hai aage badhna padega)
        g+=1
    else:
        b+=1
print(pair)