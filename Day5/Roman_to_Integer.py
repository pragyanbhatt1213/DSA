class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total=0
        i=0
        while(i<len(s)):
            if(i<len(s)-1):
                a=roman_map[(s[i])]
                b=roman_map[(s[i+1])]
                if(a>=b):
                    total+=a
                    i+=1
                elif(a<b):
                    total+=b-a
                    i+=2
            else:
                total+=(roman_map[(s[i])])
                i+=1
        return(total)

sol = Solution()
print(sol.romanToInt("III"))  
print(sol.romanToInt("MCMXCIV")) 

