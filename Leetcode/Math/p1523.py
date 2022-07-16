## 1523. Count Odd Numbers in an Interval Range

# Example 1:
# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].

# Example 2:
# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # count = 0
        # for x in range(low, high+1):
        #     if x%2!=0:
        #         count+=1
        if low%2!=0 and high%2!=0:     
            return (high-low+1)//2+1
        elif low%2!=0 or high%2!=0:
            return (high-low+1)//2
        else:
            return (high-low)//2