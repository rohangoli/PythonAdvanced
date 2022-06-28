# Maximum XOR of Two Numbers in an Array

# Example 1:
# Input: nums = [3,10,5,25,2,8]
# Output: 28
# Explanation: The maximum result is 5 XOR 25 = 28.

# Example 2:
# Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isLast = False

class Solution:  
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num: int) -> None:
        curr = self.root
        
        ## 0 <= nums[i] <= 2**31 - 1 >>> Most Significant Bit = 2**30
        for i in range(30,-1,-1):
            bit = bool(num & (1 << i))
            if bit not in curr.children:
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]
            
        return None
    
    def query(self, key, otherKey) -> int:
        XOR = 0
        curr = self.root
        
        for i in range(30,-1,-1):
            bit = bool(key & (1 << i))
            if (not bit) in curr.children:
                curr = curr.children[not bit]
                XOR = XOR | (1<<i)
                
                if not bit:
                    otherKey = otherKey | (1<<i)
                else:
                    otherKey = otherKey & (1<<i)
            else:
                if bit:
                    otherKey = otherKey | (1<<i)
                else:
                    otherKey = otherKey & (1<<i)
                curr = curr.children[bit]
                
        return XOR
    
    def getMax(self, num) -> int:
        curr = self.root
        maxXOR = 0
        
        for i in range(30,-1,-1):
            bit = bool(num & (1 << i))
            if (not bit) in curr.children:
                maxXOR = maxXOR | (1<<i)
                curr = curr.children[not bit]
            else:
                curr = curr.children[bit]
                
        return maxXOR               

    
    def findMaximumXOR(self, nums: List[int]) -> int:
        ## Trie Implementation
        ## 1. Insert Elements
        ## 2. Find Max
        ## 3. Return Max
        
        ## Insert Elements into Trie DS
        for x in nums:
            self.insert(x)
            
        ## Find Max XOR combination
        maxi = 0
        for x in nums:
            maxi = max(maxi, self.getMax(x))
            
        return maxi
    
    def findMaximumXOR_V2(self, nums: List[int]) -> int:
        ## O(N. Log N) - TC >>> Trie Implementation
        
        maxXOR = 0
        if len(nums)<2:
            return 0
        
        self.insert(0)
        for x in nums:
            elem = 0
            curr = self.query(x, elem)
            #print(x,curr)
            
            if curr > maxXOR:
                maxXOR = curr
            
            self.insert(x)
            
        return maxXOR

    
    def findMaximumXOR_V3(self, nums: List[int]) -> int:
        ## O(N**2) - TC
        ## O(1) - SC
        result = 0
        N = len(nums)
        i=0
        while i<N:
            j=i+1
            while j<N:
                temp = nums[i]^nums[j]
                if temp>result:
                    print(nums[i],nums[j])
                    result=temp
                j+=1
            i+=1
                    
        return result

