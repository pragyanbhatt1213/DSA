x=input()
d=0
for i in x:
    if(i=='4' or i=='7'):
        d+=1
        break
x=int(x)
if(d>0):
    print("YES")

elif(x%47==0 or x%4==0 or x%7==0):
    print("YES")
else:
    print("NO")