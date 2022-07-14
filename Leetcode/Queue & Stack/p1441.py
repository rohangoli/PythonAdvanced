## 1441. Build an Array With Stack Operations

# Example 1:
# Input: target = [1,3], n = 3
# Output: ["Push","Push","Pop","Push"]
# Explanation: 
# Read number 1 and automatically push in the array -> [1]
# Read number 2 and automatically push in the array then Pop it -> [1]
# Read number 3 and automatically push in the array -> [1,3]

# Example 2:
# Input: target = [1,2,3], n = 3
# Output: ["Push","Push","Push"]

# Example 3:
# Input: target = [1,2], n = 4
# Output: ["Push","Push"]
# Explanation: You only need to read the first 2 numbers and stop.

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ## Stack Implementation
        value = 1
        ptr2 = 0
        tempS = []
        result = []
        while value<=n:
            if tempS==target:
                break
            
            tempS.append(value)
            result.append("Push")
            
            if target[ptr2]==(value):
                ptr2+=1
            else:
                tempS.pop()
                result.append("Pop")
                
            value+=1
            
        return result

    def buildArray_v2(self, target: List[int], n: int) -> List[str]:
        ## Array Implementation - Faster than Stack / Requires Less Memory
        tempArr = [_ for _ in range(1,n+1)]
        #print(tempArr)
        result = []
        i=0
        j=0
        while i<len(target) and j<n and tempArr[j]<=target[i]:
            #print(result, i, j)
            if target[i]==tempArr[j]:
                result.append("Push")
                i+=1
            else:
                result.append("Push")
                result.append("Pop")
                
            j+=1
        
        return result
            
            
            