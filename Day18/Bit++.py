n=int(input())
x=0
for _ in range(n):
    string=input().strip()
    if '+' in string:
        x+=1
    else:
        x-=1
print(x)
