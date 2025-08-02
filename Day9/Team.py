n = int(input())
l = []
for _ in range(n):
    a = list(map(int, input().split()))
    l.append(a)
d=0
for i in l:
    two=0
    if(i[0]==1):
        two+=1
    if(i[1]==1):
        two+=1
    if(i[2]==1):
        two+=1
    if(two>=2):
        d+=1
print(d)
