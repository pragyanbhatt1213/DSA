n=int(input())
coin=list(map(int, input().split()))
coin.sort()
mySum=0
count=0
total=sum(coin)
for i in range(len(coin)-1, -1, -1):
    mySum+=coin[i]
    count+=1
    if(mySum>(total-mySum)):
        break
print(count)


