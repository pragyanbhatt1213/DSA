s1=input()
s2=input()
result=""
for i in range(len(s1)):
    if(s1[i]!=s2[i]):
        result+='1'
    else:
        result+='0'
print(result)
