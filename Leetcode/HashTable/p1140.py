## Design HashMap

# Example 1:
# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

class MyHashMap:

    def __init__(self):
        self.hash = 1000001
        self.arr = [-1 for _ in range(self.hash)]

    def put(self, key: int, value: int) -> None:
        self.arr[key]=value
        # print(self.arr)
        return None

    def get(self, key: int) -> int:
        # print(self.arr)
        return self.arr[key]

    def remove(self, key: int) -> None:
        self.arr[key]=-1
        # print(self.arr)
        return None  
    
#     def __init__(self):
#         self.hash = 1000
#         self.arr = [[] for _ in range(self.hash)]

#     def put(self, key: int, value: int) -> None:
#         if self.arr[key%self.hash]==[]:
#             self.arr[key%self.hash].append(value)
#         else:
#             self.arr[key%self.hash]=[value]
#         return None

#     def get(self, key: int) -> int:
#         if self.arr[key%self.hash]!=[]:
#             return self.arr[key%self.hash]
#         else:
#             return -1

#     def remove(self, key: int) -> None:
#         if self.arr[key%self.hash]!=[]:
#             self.arr[key%self.hash]=[]
#         return None       


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)