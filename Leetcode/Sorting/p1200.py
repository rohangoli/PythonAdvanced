## 1200. Minimum Absolute Difference

import math
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        
        minDiff = math.inf
        result = []
        i=0
        while i<len(arr)-1:
            temp = abs(arr[i]-arr[i+1])
            if temp<minDiff:
                minDiff = temp
                result = [[arr[i],arr[i+1]]]
            elif temp==minDiff:
                result.append([arr[i],arr[i+1]])
            
            i+=1
            
        return result
                