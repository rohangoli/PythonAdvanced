## Height Checker

# Example 1:
# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation: 
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.

# Example 2:
# Input: heights = [5,1,2,3,4]
# Output: 5
# Explanation:
# heights:  [5,1,2,3,4]
# expected: [1,2,3,4,5]
# All indices do not match.

# Example 3:
# Input: heights = [1,2,3,4,5]
# Output: 0
# Explanation:
# heights:  [1,2,3,4,5]
# expected: [1,2,3,4,5]
# All indices match.

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        N=len(heights)
        
        expected = heights.copy()
        expected.sort()
        
        result=0
        for x,y in zip(heights,expected):
            if x!=y:
                result+=1
        
        return result
    
#     def heightChecker(self, heights: List[int]) -> int:
#         N=len(heights)
        
#         i=0
#         result=0
#         while i<N:
#             j=N-1
#             while heights[i]>heights[j]:
#                 heights[i],heights[j]=heights[j],heights[i]
#                 result+=1
#                 j-=1
#             print(heights)
#             i+=1
        
#         if result>0:
#             result+=1
            
#         return result
        