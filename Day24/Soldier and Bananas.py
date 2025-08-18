k,n,w= map(int, input().split())
s=k*w*(w+1)//2
 

if(s-n>0):
    print(s-n)
else:
    print(0)
