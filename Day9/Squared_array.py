class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        arr=[]
        while(left<=right):
            if(abs(nums[left])>=abs(nums[right])):
                value=nums[left]**2
                arr.append(value)
                left+=1
                
            else:
                value=nums[right]**2
                arr.append(value)
                right-=1
                
        return(arr[::-1])