class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max=''
        for i in range(len(num)-2):
            if(num[i]==num[i+1]==num[i+2]):
                if(num[i]>max):
                    max=num[i]
        return(max*3)
                