## Top K Frequent Elements

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## Rohan's solution - O(NlogN)
        maxFreq=0
        temp=Counter()
        for x in nums:
            temp[x]+=1
            maxFreq=max(maxFreq,temp[x])
        print(temp, maxFreq, k)    
        
        temp2 = sorted(temp.values())[-k:]
        
        result=[]
        for key, value in temp.items():
            if value in temp2:
                result.append(key)
                temp2.remove(value)
                
        return result
            
        # result=[]
        # for key,value in temp.items():
        #     if value>=k:
        #         result.append(key)
        # return result

    def topKFrequent_v2(self, nums: List[int], k: int) -> List[int]:
        numDict = {}
        for num in nums:
            if num not in numDict:
                numDict[num] = 1
            else:
                numDict[num]+= 1
        return((sorted(numDict, key = numDict.get, reverse=True))[0:k])