#one way
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        common=[]
        i,j=0,0
        while i < len(nums1) and j < len(nums2):
            if(nums1[i]<nums2[j]):
                i+=1
            elif(nums1[i]>nums2[j]):
                 j+=1
            else:
                common.append(nums1[i])
                j+=1
                i+=1
        return(common)             
    
    #More efficeint way
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1={}
        freq2={}
        for i in nums1:
            if(i in freq1):
                freq1[i]+=1
            else:
                freq1[i]=1
        for i in nums2:
            if(i in freq2):
                freq2[i]+=1
            else:
                freq2[i]=1
        result=[]
        for i in freq1:
            if i in freq2.keys():
                min_occur=min(freq1[i],freq2[i])
                result += [i]*min_occur
        return(result)

            

        
        