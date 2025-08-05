class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        left=0
        right=len(height)-1
        while(left<right):
            curr_area=min(height[left], height[right])*(right-left)#Area nikal rhe
            if(curr_area>max_area):
                max_area=curr_area

            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
    
        return(max_area)