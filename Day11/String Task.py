word=input()
word=word.lower()
result=""
for i in word:
    if(i=='a'or i=='e'or i=='o' or i=='i' or i=='u' or i=='y'):
        continue
    else:
        result+="."+i
print(result)