n= int(input())
word_list=[]
for _ in range(n):
    s=input()
    word_list.append(s)
for word in word_list:
    if(len(word)>10):
        a=str(word[0:1])
        b=str((len(word))-2)
        c=str(word[-1])
        print(a+b+c)
    else:
        print(word)