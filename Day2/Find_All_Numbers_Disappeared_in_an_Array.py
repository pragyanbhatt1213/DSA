from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)):
            x=abs(nums[i])
            nums[x-1]=-abs(nums[x-1])
        l=[]
        for i in range(0,len(nums)):
            if(nums[i]>0):
                l.append(i+1)
        return(l)
            

sol = Solution()

print("Test Case 1:")
nums1 = [4,3,2,7,8,2,3,1]
print(f"Input: {nums1}")
result1 = sol.findDisappearedNumbers(nums1)
print(f"Output: {result1}")
print(f"Expected: [5,6]\n")

print("Test Case 2:")
nums2 = [1,1]
print(f"Input: {nums2}")
result2 = sol.findDisappearedNumbers(nums2)
print(f"Output: {result2}")
print(f"Expected: [2]\n")

print("Test Case 3:")
nums3 = [1,2,3,4]
print(f"Input: {nums3}")
result3 = sol.findDisappearedNumbers(nums3)
print(f"Output: {result3}")
print(f"Expected: []\n")

print("Test Case 4:")
nums4 = [1,1,1,1,1]
print(f"Input: {nums4}")
result4 = sol.findDisappearedNumbers(nums4)
print(f"Output: {result4}")
print(f"Expected: [2,3,4,5]\n")

print("Test Case 5:")
nums5 = [3,2,1]
print(f"Input: {nums5}")
result5 = sol.findDisappearedNumbers(nums5)
print(f"Output: {result5}")
print(f"Expected: []\n")

print("Test Case 6:")
nums6 = [1,3,3]
print(f"Input: {nums6}")
result6 = sol.findDisappearedNumbers(nums6)
print(f"Output: {result6}")
print(f"Expected: [2]\n")
