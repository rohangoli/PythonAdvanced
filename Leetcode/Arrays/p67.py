## Add Binary

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        M = len(a)
        N = len(b)
        
        O = max(M,N)
        
        A = ['0']*(O-M) + [x for x in a]
        B = ['0']*(O-N) + [x for x in b]
        
        print(A,B)
        print(O)
        
        i=O-1
        carryOn = '0'
        result=['0']*O
        while i>=0:
            if A[i]=='0' and B[i]=='0':
                result[i]=carryOn
                carryOn='0'
            elif (A[i]=='1' and B[i]=='0') or (A[i]=='0' and B[i]=='1'):
                if carryOn=='1':
                    result[i]='0'
                    carryOn='1'
                else:
                    result[i]='1'
                    carryOn='0'
            else:
                if carryOn=='1':
                    result[i]='1'
                    carryOn='1'
                else:
                    result[i]='0'
                    carryOn='1'
            print(result)
            i-=1
            
        if carryOn=='1':
            return "".join(['1']+result)
        else:
            return "".join(result)