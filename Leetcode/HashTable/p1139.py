## Design HashSet

# Example 1:
# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]

# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)

class MyHashSet:
    
#     def __init__(self):
#         self.arr = []

#     def add(self, key: int) -> None:
#         if key not in self.arr:
#             self.arr.append(key)
#         return None

#     def remove(self, key: int) -> None:
#         if key in self.arr: 
#             self.arr.remove(key)
#         return None

#     def contains(self, key: int) -> bool:
#         if key in self.arr:
#             return True
#         else:
#             return False


    def __init__(self):
        self.hash = 1000
        self.arr = [[] for i in range(1000)]
        # print(self.arr)

    def add(self, key: int) -> None:
        if key not in self.arr[key%self.hash]:
            self.arr[key%self.hash].append(key)
        return None

    def remove(self, key: int) -> None:
        if key in self.arr[key%self.hash]: 
            self.arr[key%self.hash].remove(key)
        return None

    def contains(self, key: int) -> bool:
        if key in self.arr[key%self.hash]:
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)