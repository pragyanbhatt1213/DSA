from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq={}
        l=[]
        for i in nums:
            if(i in freq):
                freq[i]+=1
            else:
                freq[i]=1
        for n,f in freq.items():
            if(f>1):
                l.append(n)
        return(l)

        