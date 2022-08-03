## 121. Best Time to Buy and Sell Stock

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## O(n^2) - TC
#         result = 0
#         N = len(prices)
#         i=0
#         while i<N-1:
#             j=i+1
#             while j<N:
#                 result = max(result, prices[j]-prices[i])
#                 j+=1 
#             i+=1
            
#         if result<0:
#             return -1
#         else:
#             return result
        
        ## O(n) - TC
        result = 0
        N = len(prices)
        slow=0
        fast=1
        while fast<N:
            if prices[fast]<prices[slow]:
                slow=fast
            result = max(result, prices[fast]-prices[slow])
            fast+=1
            
        return result