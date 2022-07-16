## 657. Robot return to the origin

# Example 1:
# Input: moves = "UD"
# Output: true
# Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.

# Example 2:
# Input: moves = "LL"
# Output: false
# Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        posX, posY = 0,0
        for move in moves:
            if move=='U':
                posY+=1
            elif move=='D':
                posY-=1
            elif move=='L':
                posX-=1
            else:
                posX+=1
        
        return posX==0 and posY==0