n=int(input())
a=list(map(int, input().split()))

max_height=max(a)
min_height=min(a)

max_index=a.index(max_height)
min_index=len(a)-1-a[::-1].index(min_height)

if max_index>min_index:
    print(max_index+n-1-min_index-1)
else:
    print(max_index+n-1-min_index)
