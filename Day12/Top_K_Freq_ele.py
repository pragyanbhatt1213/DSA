from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        heap=[]
        for i in nums:
            if(i in freq):
                freq[i]+=1
            else:
                freq[i]=1
        for n,f in freq.items():
            heapq.heappush(heap,(f,n))
            if len(heap) > k:
                heapq.heappop(heap)
        result=[]
        for i in range(k):
            a=heapq.heappop(heap)
            result.append(a[1])
        return(result[::-1])
        

            

sol = Solution()

print("Test Case 1:")
nums1 = [1,1,1,2,2,3]
k1 = 2
print(f"Input: nums = {nums1}, k = {k1}")
# result1 = sol.topKFrequent(nums1, k1) # Uncomment to run your full code
# print(f"Output: {result1}")
print(f"Expected: [1,2] (order may vary)\n")
sol.topKFrequent(nums1,k1)


# print("Test Case 2:")
# nums2 = [1]
# k2 = 1
# print(f"Input: nums = {nums2}, k = {k2}")
# # result2 = sol.topKFrequent(nums2, k2) # Uncomment to run your full code
# # print(f"Output: {result2}")
# print(f"Expected: [1]\n")

# print("Test Case 3: More complex, multiple same frequencies")
# nums3 = [1,2,3,4,5,1,2,3,1,2,1]
# k3 = 3
# print(f"Input: nums = {nums3}, k = {k3}")
# # result3 = sol.topKFrequent(nums3, k3) # Uncomment to run your full code
# # print(f"Output: {result3}")
# print(f"Expected: [1,2,3] (order may vary for 2,3)\n")

# print("Test Case 4: All unique elements")
# nums4 = [10,20,30,40,50]
# k4 = 5
# print(f"Input: nums = {nums4}, k = {k4}")
# # result4 = sol.topKFrequent(nums4, k4) # Uncomment to run your full code
# # print(f"Output: {result4}")
# print(f"Expected: [10,20,30,40,50] (order may vary)\n")

# print("Test Case 5: Large k, small nums")
# nums5 = [7,7,7,8,8,9]
# k5 = 2
# print(f"Input: nums = {nums5}, k = {k5}")
# # result5 = sol.topKFrequent(nums5, k5) # Uncomment to run your full code
# # print(f"Output: {result5}")
# print(f"Expected: [7,8] (order may vary)\n")