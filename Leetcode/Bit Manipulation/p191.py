## 191. Number of 1 Bits

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
        
        # bits=32
        # result = 0
        # print(str(n))
        # while bits>0:
        #     temp = n%2
        #     print(n, temp)
        #     if temp==1:
        #         result+=1
        #     n = n/10
        #     print(n)
        #     bits-=1
            
        return 0