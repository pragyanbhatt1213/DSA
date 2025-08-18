s=input()
upper,lower=0,0
for i in s:
    if(i.islower()):
        lower+=1
    else:
        upper+=1
if(upper>lower):
    print(s.upper())
else:
    print(s.lower())