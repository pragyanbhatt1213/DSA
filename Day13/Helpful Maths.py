
s = "3+2+1"
l = list(map(int, s.split('+')))
freq={}
reslut=""
for i in l:
    if(i in freq):
        freq[i]+=1
    else:
        freq[i]=1
for n,f in freq.items():
    reslut+=str(n)*f
print('+'.join(reslut))
        

