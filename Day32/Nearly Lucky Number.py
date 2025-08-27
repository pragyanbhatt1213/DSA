n=input()
d=0
for i in n:
    if(i=='4' or i=='7'):
        d+=1
if all(c in '47' for c in str(d)):
    print("YES")
else:
    print("NO")
