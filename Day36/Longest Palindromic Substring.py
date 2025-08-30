class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str=""
        curr_len=0
        for i in range(len(s)):
            left=i
            right=i
            while(left>=0 and right<len(s) and s[left]==s[right]):
                if (right-left+1)>curr_len:
                    max_str=s[left:right+1]
                    curr_len=right-left+1
                left-=1
                right+=1
            left=i
            right=i+1
            while(left>=0 and right<len(s) and s[left]==s[right]):
                if(right-left+1)>curr_len:
                    max_str=s[left:right+1]
                    curr_len=right-left+1
                left-=1
                right+=1
        return(max_str)
sol = Solution()
print(sol.longestPalindrome("babad"))   
print(sol.longestPalindrome("cbbd"))  
print(sol.longestPalindrome("a"))     
print(sol.longestPalindrome("ac"))     
print(sol.longestPalindrome("abacdfgdcaba"))

