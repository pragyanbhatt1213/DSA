class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxPro=nums[0]
        minPro=nums[0]
        final=nums[0]
        for i in nums[1:]:
            if(i<0):
                maxPro,minPro=minPro,maxPro
            minPro=min(i,i*minPro)
            maxPro=max(i,i*maxPro)
            final=max(maxPro,final)

        return(final)