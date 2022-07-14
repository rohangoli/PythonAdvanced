## 1475. Final Prices With a Special Discount in a Shop

# Example 1:
# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
# Explanation: 
# For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4. 
# For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2. 
# For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4. 
# For items 3 and 4 you will not receive any discount at all.

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: [1,2,3,4,5]
# Explanation: In this case, for all items, you will not receive any discount at all.

# Example 3:
# Input: prices = [10,1,1,6]
# Output: [9,0,1,6]
 
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        result = []
        
        tempS = []
        tempArr = []
        
        N = len(prices)
        
        i = N-1
        while i>-1:
            #print(i, prices[i], tempS, tempArr)
            while tempS and tempS[-1]>prices[i]:
                tempS.pop()
                
            if not tempS:
                tempArr.append(0)
            else:
                tempArr.append(tempS[-1])
                
            tempS.append(prices[i])
            i-=1
            
        #print(tempArr)
        
        i = 0
        while i<N:
            result.append(prices[i]-tempArr[N-i-1])
            i+=1
        
        return result