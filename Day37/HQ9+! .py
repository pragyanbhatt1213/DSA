s=input()
d=0
for i in s:
    if(i  in {'H', 'Q', '9'}):
        d+=1
        break
if(d>0):
    print("YES")
else:
    print("NO")