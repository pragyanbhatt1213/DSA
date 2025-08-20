s=input()
n=len(s)
found=False
for i in range(n-6):
        if(s[i:(i+7)]=='1111111' or s[i:(i+7)]=='0000000'):
            found=True
if(found):
      print("YES")
else:
      print("NO")
