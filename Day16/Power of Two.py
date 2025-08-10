class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n==1):
            return(True)
        if(n<1):
            return(False)
        while(True):
            n=n//2
            if(n%2!=0):
                return(False)
            if(n==1):
                return(True)
        return(False)
            