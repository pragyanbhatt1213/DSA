from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common=[0]*26
        for i in words[0]:
            a=ord(i)-ord('a')
            common[a]+=1

        for i in words[1:]:
            counts=[0]*26
            for char in i:
                a=ord(char)-ord('a')
                counts[a]+=1
            
            for j in range(26):
                common[j]=min(common[j],counts[j])
        result = []
        for i in range(26):
            if common[i] > 0:
                result += [chr(i + ord('a'))] * common[i]
        return result

                

