## Spiral Matrix

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowLB=0
        rowUB=len(matrix)
        
        colLB=0
        colUB=len(matrix[0])
        
        N = rowUB*colUB
        result=[]
        
        i=0
        x=0
        y=0
        rowUB-=1
        colUB-=1
        while i<N:
            x=rowLB
            y=colLB
            while y<colUB+1 and i<N:
                print(x,y)
                result.append(matrix[x][y])
                i+=1
                y+=1
            rowLB+=1
            print('----',rowLB,rowUB,'----',colLB,colUB,'----',i)
            
            y=colUB
            x+=1
            while x<rowUB+1 and i<N:
                print(x,y)
                result.append(matrix[x][y])
                i+=1
                x+=1
            colUB-=1
            print('----',rowLB,rowUB,'----',colLB,colUB,'----',i)
            
            x=rowUB
            y-=1
            while y>colLB-1 and i<N:
                print(x,y)
                result.append(matrix[x][y])
                i+=1
                y-=1
            rowUB-=1
            print('----',rowLB,rowUB,'----',colLB,colUB,'----',i)
            
            y=colLB
            x-=1
            while x>rowLB-1 and i<N:
                print(x,y)
                result.append(matrix[x][y])
                i+=1
                x-=1
            colLB+=1
            print('----',rowLB,rowUB,'----',colLB,colUB,'----',i)
            
            # print(rowLB, rowUB)
            # print(colLB, colUB)
            
            # print(matrix[x][y])
            
        return result
