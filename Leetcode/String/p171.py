## 171. Excel Sheet Column Number

# Example 1:
# Input: columnTitle = "A"
# Output: 1

# Example 2:
# Input: columnTitle = "AB"
# Output: 28

# Example 3:
# Input: columnTitle = "ZY"
# Output: 701

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        mapAlpha = {chr(x):x-64 for x in range(65,91)}
        #print(mapAlpha)
        
        result = 0
        power = 0
        for x in columnTitle[::-1]:
            result+= mapAlpha[x]*(26**power)
            power+=1
            
        return result
        
#         N = len(columnTitle)
#         j = N-1
#         result = 0
#         power = 0
#         while j>-1:
#             result+= mapAlpha[columnTitle[j]]*power
#             power+=1
#             j-=1
            
#         return result


