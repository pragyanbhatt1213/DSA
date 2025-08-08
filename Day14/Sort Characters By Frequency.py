import heapq
from typing import List
class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        heap=[]
        result=""
        for i in s:
            if(i in freq):
                freq[i]+=1
            else:
                freq[i]=1
        for n,f in freq.items():
            heapq.heappush(heap,(-f,n))
        for i in range(len(heap)):
            a=heapq.heappop(heap)
            result+=(str(a[1]))*(-a[0])      
        return(result)
     