class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x%10==0 and x!=0):
            return(False)
        n=x
        s=0
        while(n>0):
            s=s*10+(n%10)
            n=n//10
        if(s==x):
            return(True)
        else:
            return(False)        