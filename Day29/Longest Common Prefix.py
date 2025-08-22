class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str1 = min(strs) #flight
        str2 = max(strs) #flower
        i = 0
        while i < len(str1):
            if str1[i] != str2[i]:
                str1 = str1[:i]
            i += 1
        return str1