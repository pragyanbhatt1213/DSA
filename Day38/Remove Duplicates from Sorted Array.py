class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a,b=0,1
        while b in range(len(nums)):
            if nums[a] ==nums[b]:
                b+=1
            else:
                nums[a+1]=nums[b]
                b+=1
                a+=1
        return a+1
        