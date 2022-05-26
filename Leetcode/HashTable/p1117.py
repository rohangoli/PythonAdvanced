## Isomorphic Strings

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sDict={}
        for idx,x in enumerate(s):
            if x in sDict:
                sDict[x].append(idx)
            else:
                sDict[x]=[idx]
                
        tDict={}
        for idx,x in enumerate(t):
            if x in tDict:
                tDict[x].append(idx)
            else:
                tDict[x]=[idx]
        
        # print(sDict,tDict)
        # print(list(sDict.values()))
        # print(list(tDict.values()))
        if list(sDict.values()) == list(tDict.values()):
            return True
        else:
            return False