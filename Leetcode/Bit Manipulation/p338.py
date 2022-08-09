## 338. Counting Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        result=0
        while n>0:
            temp = n%2
            #print(n, temp)
            if temp==1:
                result+=1
            n=n//2    
        return result
    
    def countBits(self, n: int) -> List[int]:
        output = []
        for x in range(n+1):
            output.append(self.hammingWeight(x))
            
        return output