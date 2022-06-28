## 867. Transpose Matrix

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]

# Example 2:
# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        M = len(matrix)
        N = len(matrix[0])
        
        result = []
        
        i=0
        while i<N:
            temp = []
            j=0
            while j<M:
                temp.append(matrix[j][i])
                j+=1
            result.append(temp)
            i+=1
        
        return result