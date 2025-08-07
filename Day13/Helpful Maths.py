s = input()
l = list(map(int, s.split('+')))
freq={}
reslut=""
for i in l:
    if(i in freq):
        freq[i]+=1
    else:
        freq[i]=1
for n in sorted(freq):
    reslut += (str(n) + '+') * freq[n]
print(reslut.rstrip('+'))
        

