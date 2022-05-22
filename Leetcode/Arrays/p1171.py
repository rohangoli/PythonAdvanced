## Pascal's Triangle II

# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:
# Input: rowIndex = 0
# Output: [1]

# Example 3:
# Input: rowIndex = 1
# Output: [1,1]

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result=[]
        
        i=1
        while i<rowIndex+2:
            if i<=2:
                result.append([1]*i)
            else:
                temp = [1]*i
                j=1
                while j<i-1:
                    temp[j]=result[-1][j-1]+result[-1][j]
                    j+=1
                result.append(temp)
            print(result)
            i+=1
        return result[-1]