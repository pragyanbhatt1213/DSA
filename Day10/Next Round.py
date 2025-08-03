n,k=map(int,input().split())
l=list(map(int,input().split()))
d=0
for score in l:
    if(score>=l[k-1] and score>0):
        d+=1
print(d)
