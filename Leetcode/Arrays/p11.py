## 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        i=0
        j=len(height)-1
        
        while i<j:
            #print('left({})-{} right({})-{}'.format(i,height[i],j,height[j]))
            if height[i]<height[j]:
                result = max(result, height[i]*(j-i))
                i+=1
            else:
                result = max(result, height[j]*(j-i))
                j-=1
            #print(result)
                
        return result