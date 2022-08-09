## Reverse Bits

class Solution:
    def reverseBits(self, n: int) -> int:
        def int2base(x):
            result = []
            while x>0:
                result.append(x%2)
                x//=2
            return result
        
        def base2int(x):
            result = 0
            i=0
            while i<len(x):
                #print(result, result*2, x[i])
                result = result*2 + x[i]
                i+=1
                
            return result
        
        temp = int2base(n)
        temp = temp + [0]*(32-len(temp))
        return base2int(temp)