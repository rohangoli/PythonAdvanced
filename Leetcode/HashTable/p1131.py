## Happy Number

# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# Example 2:
# Input: n = 2
# Output: false

class Solution:
    def isHappy(self, n: int) -> bool:
        
        tempSet=set()
        while n not in tempSet:
            temp = n
            tempSet.add(n)
            n=0
            while temp>0:
                n+=(temp%10)**2
                temp=temp//10
            # print(n)
        # print('='*25)
        if n==1:
            return True
        else:
            return False