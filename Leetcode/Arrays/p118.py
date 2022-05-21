## Pascals Triangle

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        i=1
        result = []
        while i<numRows+1:
            if i==1:
                result.append([1])
            elif i==2:
                result.append([1,1])
            else:
                temp=[]
                j=0
                while j<i-2:
                    temp.append(result[-1][j]+result[-1][j+1])
                    j+=1
                result.append([1]+temp+[1])
            i+=1
        return result