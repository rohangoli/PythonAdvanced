## Plus One

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)
        
        j=N-1
        carryOn = 0        
        ## Add One to least significatn digit
        digits[j] = digits[j]+1

        while j>-1:
            newNum = digits[j]+carryOn
            if newNum>9:
                carryOn = 1
                digits[j]= newNum - 10
            else:
                carryOn=0
                digits[j]=newNum

            j-=1
        
        if carryOn == 0:
            return digits
        else:
            return [carryOn]+digits