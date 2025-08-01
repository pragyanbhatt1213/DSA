#Without carry
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if(digits[i]==9):
                digits[i]=0
            else:
                digits[i]+=1
                return(digits)
        digits.insert(0,1)
        return(digits)

# with carry count
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d=1
        for i in range(len(digits)-1,-1,-1):
            digits[i]+=d
            if(digits[i]==9):
                digits[i]=0
                d+=1
            else:
                d=0
                break
        if(d>0):
            digits=digits.insert(0,1)
            return(digits)
        else:
            return(digits)            

