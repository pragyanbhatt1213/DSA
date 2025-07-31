
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        for i in range(len(strs)):
            counts = [0] * 26
            for j in strs[i]:
                c=ord(j) - ord('a')
                counts[c]+=1
            counts=tuple(counts)
            group[counts].append(strs[i])
        return(group.values())
        
sol = Solution()

print("Test Case 1:")
strs1 = ["eat","tea","tan","ate","nat","bat"]
print(f"Input: strs = {strs1}")
result1 = sol.groupAnagrams(strs1)
print(f"Output: {result1}")

print("Test Case 2:")
strs2 = [""]
print(f"Input: strs = {strs2}")
result2 = sol.groupAnagrams(strs2)
print(f"Output: {result2}")