class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in  range(len(s)):
            if(s[i].isalnum()):
                a+=(s[i].lower())
        left=0
        right=len(a)-1
        while(left<right):
            if(a[left]!=a[right]):
                return(False)
            left+=1
            right-=1
        return(True)
    

sol = Solution()

# Test cases
inputs = [
    "A man, a plan, a canal: Panama",  # True
    "race a car",                      # False
    "",                                # True
    "1a2",                             # False
    "No 'x' in Nixon",                 # True
    "Was it a car or a cat I saw?",   # True
]

# Run and print results
for s in inputs:
    print(f"Input: {s!r}")
    print(f"Output: {sol.isPalindrome(s)}\n")