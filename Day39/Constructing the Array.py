import sys
import heapq
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    result=[0]*n
    heap=[(-n,0,n-1)]  # (length, left, right)
    i=1
    while heap:
        length,l,r=heapq.heappop(heap)
        length=-length   # actual positive length
        mid=(l+r)//2     # always middle index
        result[mid]=i
        i+=1
        # Left segment
        if l <= mid-1:
            new_len = (mid-1) - l + 1   # correct length
            heapq.heappush(heap, (-new_len, l, mid-1))
        # Right segment
        if mid+1 <= r:
            new_len = r - (mid+1) + 1   # correct length
            heapq.heappush(heap, (-new_len, mid+1, r))
    print(*result)
