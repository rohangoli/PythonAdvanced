##  Flood Fill

# Example 1:
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

# Example 2:
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation: The starting pixel is already colored 0, so no changes are made to the image.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        tempS = []
        visited = set()
        
        srcColor = image[sr][sc]
        if srcColor==color or not image:
            return image
        
        M = len(image)
        N = len(image[0])
        tempS = [(sr,sc)]
        
        while tempS:
            #print(tempS)
            currX,currY = tempS.pop()
            # print(currX, currY)
            
            if (currX,currY) in visited:
                continue
            
            image[currX][currY] = color
            visited.add((currX,currY))
            
            if currX<M-1 and image[currX+1][currY]==srcColor:
                tempS.append((currX+1, currY))
            if currY<N-1 and image[currX][currY+1]==srcColor:
                tempS.append((currX, currY+1))
            if currX>0 and image[currX-1][currY]==srcColor:
                tempS.append((currX-1, currY))
            if currY>0 and image[currX][currY-1]==srcColor:
                tempS.append((currX, currY-1))
                
        return image
                
            