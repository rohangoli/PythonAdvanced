## Group Anagrams

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp={}
        for x in strs:
            ang = ''.join(sorted(x))
            # print(ang)
            if ang in temp:
                temp[ang].append(x)
                continue
            temp[ang]=[x]
        
        return list(temp.values())