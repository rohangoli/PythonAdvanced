# Diagonal Traverse

# Example 1
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]

# Example 2:
# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        M = len(mat)
        N = len(mat[0])
        
        slices = M+N - 1
        
        i=0
        result = []
        j=1
        while i<slices:
            temp=[]
            r = 0 if i<N else i-N+1
            c = i if i<N else N-1

            while r<M and c>-1:
                #print(r,c)
                temp.append(mat[r][c])
                r+=1
                c-=1

            if j==0:
                result.extend(temp)
                j=1
            else:
                result.extend(temp[::-1])
                j=0
            i+=1
            
        return result