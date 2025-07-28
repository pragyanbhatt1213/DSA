from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            n=nums[i]
            c=target-n
            if c in seen:
                return[seen[c],i]
            seen[n]=i
        
        


sol = Solution()

print("Test Case 1:")
nums1 = [2,7,11,15]
target1 = 9
print(f"Input: nums = {nums1}, target = {target1}")
result1 = sol.twoSum(nums1, target1)
print(f"Output: {result1}")