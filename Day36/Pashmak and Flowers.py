n=int(input())
beauties=list(map(int,input().split()))
mn=min(beauties)
mx=max(beauties)
if mn==mx:
    ways=n*(n-1)//2
    print(0,ways)
else:
    cnt_min=beauties.count(mn)
    cnt_max=beauties.count(mx)
    diff=mx-mn
    ways=cnt_min*cnt_max
    print(diff,ways)
