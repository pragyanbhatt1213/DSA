class Solution:
    def longestPalindrome(self, s: str) -> int:
        count={}
        for i in s:
            if(i in count):
                count[i]+=1
            else:
                count[i]=1
        length=0
        found=False
        for k in count.values():
            length+=(k//2)*2
            if k%2==1:
                found=True
        if found:
            length+=1
        return length
