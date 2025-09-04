class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        curr_sum=0
        min_len=len(nums)+1
        for right in range(len(nums)):
            curr_sum+=nums[right]
            while curr_sum>=target:
                curr_len=right - left+1
                min_len=min(min_len,curr_len)
                curr_sum-=nums[left]
                left+=1
        if min_len==len(nums)+1:
            return 0
        return min_len
            
#firrse krrna hai ye

