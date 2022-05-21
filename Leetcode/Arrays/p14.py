## Longest common prefix

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        print(strs)
        
        N = len(strs)
        Q = len(strs[0])
        
        if Q==0 or N==1:
            return strs[0]

        result = ""
        i=0
        while i<Q:
            base = strs[0][i]
            for j in range(1,N):
                if strs[j][i] != base:
                    return result
            result+=base
            i+=1
        return result
        
#         result = []
        
#         i=0
#         while all([strs[0][i]==x[i] for x in strs[1:]]):
#             print(all([strs[0][i]==x[i] for x in strs[1:]]))
#             result.append(strs[0][i])
#             i+=1
            
#         return "".join(result)