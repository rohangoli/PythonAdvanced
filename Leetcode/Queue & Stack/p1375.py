## Open the Lock

# Example 1:
# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation: 
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".

# Example 2:
# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".

# Example 3:
# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
# Output: -1
# Explanation: We cannot reach the target without getting stuck.

class Solution:
    def combinations(self, number: str) -> List[str]:
        number = [int(_) for _ in number]
        combinations = []
        i=0
        while i<4:
            temp1, temp2 = number.copy(), number.copy()
            temp1[i] = (temp1[i]-1)%10
            temp2[i] = (temp2[i]+1)%10
            temp1 = list(map(str,temp1))
            temp2 = list(map(str,temp2))
            # print(temp1, temp2)
            combinations.append(''.join(temp1))
            combinations.append(''.join(temp2))
            i+=1
        
        return combinations
    
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if '0000'==target:
            return 0
        
        if target in deadends or '0000' in deadends:
            return -1
        
        tempQ = ['0000']
        
        visited = set()
        for de in deadends:
            visited.add(de)
        visited.add('0000')
        # visited.append('0000')
        #print(visited)
        
        turns = 0
        while tempQ:
            size = len(tempQ)
            #print(size, tempQ)
            for i in range(size):
                curr = tempQ.pop(0)
                if curr==target:
                    #print('-'*25)
                    return turns
                #visited.add(curr)
                combs = self.combinations(curr)
                for comb in combs:
                    if comb not in visited:
                        tempQ.append(comb)
                        visited.add(comb)
            turns+=1
        #print('-'*25)    
        return -1