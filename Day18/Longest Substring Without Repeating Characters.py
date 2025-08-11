class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        freq={}
        maxlen=0
    
        for right in range(len(s)):
            char=s[right]
            if(char in freq and freq[char] >= left):
                left=freq[char]+1
            freq[char]=right
            maxlen=max(maxlen,(right-left+1))
        return(maxlen)