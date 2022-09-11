## 438. Find all Anagrams in a String

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        targetHM = Counter(p)
        sw = len(p)
        result = []
        
        ## Aproach1 - TLE : TC - O(sp)
        # i = 0
        # while i<(len(s)-sw+1):
        #     tempHM = Counter(s[i:i+sw])
        #     match = True
        #     #print(tempHM, targetHM)
        #     for k,v in targetHM.items():
        #         if k not in tempHM or tempHM[k]!=v:
        #             match=False
        #             break
        #     if match:
        #         result.append(i)
        #     i+=1
    
        ## Approach2 - Sliding HM Counter
        i = 0
        j = i+sw-1
        tempHM = Counter(s[i:j])
        while i<(len(s)-sw+1):
            tempHM[s[j]]+=1
            match = True
            #print(tempHM, targetHM)
            for k,v in targetHM.items():
                if k not in tempHM or tempHM[k]!=v:
                    match=False
                    break
            if match:
                result.append(i)
            
            tempHM[s[i]]-=1
            i+=1
            j+=1
        
        return result