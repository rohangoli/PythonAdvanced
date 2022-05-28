## Insert Delete GetRandom O(1)

# Example 1:

# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]

# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            # print(val,' already in nums - INS')
            return False
        else:
            self.nums.append(val)
            self.map[val]=len(self.nums)
            # print(self.nums, self.map)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            # print(val,' not in nums - REM')
            return False
        else:
            idx = self.map[val]
            self.map[self.nums[-1]]=idx 
            self.nums[idx-1],self.nums[-1]=self.nums[-1],self.nums[idx-1]
                       
            del self.map[val]
            self.nums.pop()

            # print(self.nums, self.map)
            return True
        

    def getRandom(self) -> int:
        # print('random')
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()