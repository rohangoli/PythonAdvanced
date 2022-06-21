## Keys and Rooms

# Example 1:
# Input: rooms = [[1],[2],[3],[]]
# Output: true
# Explanation: 
# We visit room 0 and pick up key 1.
# We then visit room 1 and pick up key 2.
# We then visit room 2 and pick up key 3.
# We then visit room 3.
# Since we were able to visit every room, we return true.

# Example 2:
# Input: rooms = [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        tempQ = [rooms[0]]
        
        visited = set()
        visited.add(0)
        
        while tempQ:
            #print(tempQ)
            curr = tempQ.pop(0)
            
            for key in curr:
                if key not in visited:
                    tempQ.append(rooms[key])
                    visited.add(key)
                    
        if len(visited)!=len(rooms):
            return False
        else:
            return True