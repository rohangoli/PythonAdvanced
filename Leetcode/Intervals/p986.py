## 986. Interval List Intersections

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        M = len(firstList)
        N = len(secondList)
        
        result = []
        i=0
        j=0
        while i<M and j<N:
            left = max(firstList[i][0], secondList[j][0])
            right = min(firstList[i][1], secondList[j][1])
            
            if left<=right:
                result.append([left,right])
                
            if firstList[i][1]<secondList[j][1]:
                i+=1
            else:
                j+=1
            
            
        return result