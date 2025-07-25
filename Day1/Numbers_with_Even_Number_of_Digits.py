from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                a += 1
        return a
    
nums1 = [12, 345, 2, 6, 7896]

nums2 = [555, 901, 482, 1771]
solution_object = Solution()
result1 = solution_object.findNumbers(nums1)
result2 = solution_object.findNumbers(nums2)

print(result1, result2)