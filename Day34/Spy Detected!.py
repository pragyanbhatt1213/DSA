t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    freq={}
    for i in arr:
        if(i in freq):
            freq[i]+=1
        else:
            freq[i]=1
    c=min(freq, key=freq.get)  #key=freq.get -> gets u the element  
    print(arr.index(c)+1)
    