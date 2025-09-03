class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result=[]
        carry=0
        x=len(a)-1
        y=len(b)-1
        while x>=0 or y>=0 or carry:
            digitA=int(a[x]) if x>=0 else 0
            digitB=int(b[y]) if y>=0 else 0
            total=digitA+digitB+carry
            result.append(str(total%2))
            carry=total//2 
            x-=1
            y-=1
        return ''.join(reversed(result))