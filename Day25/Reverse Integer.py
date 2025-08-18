class Solution:
    def reverse(self, x: int) -> int:
        sign=1
        if(x<0):
            x=abs(x)
            sign=-1
        n=x
        s=0
        while(n>0):
            s=s*10+(n%10)
            n=n//10
        s*=sign
        if(s < -2**31 or s > 2**31 - 1):
            return 0
        return s
        