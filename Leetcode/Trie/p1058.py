## Map Sum Pairs

# Example 1:
# Input
# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
# Output
# [null, null, 3, null, 5]

# Explanation
# MapSum mapSum = new MapSum();
# mapSum.insert("apple", 3);  
# mapSum.sum("ap");           // return 3 (apple = 3)
# mapSum.insert("app", 2);    
# mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.value = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        #print('-'*20)

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for char in key:
            if char not in curr.children:
                curr.children[char]=TrieNode()
                #print(char, curr.children[char])
            curr = curr.children[char]
        curr.value = val
        #print('INS complt', curr, curr.value)

    def sum(self, prefix: str) -> int:
        tempQ = []
        result = 0 
        curr = self.root
        #prev = 0
        for char in prefix:
            if char not in curr.children:
                return 0
            #result+= prev
            #prev = curr.children[char].value
            curr = curr.children[char]
        tempQ.append(curr)
        
        #print(result, curr, tempQ)
        
        while tempQ:
            #print(result, tempQ)
            curr = tempQ.pop(0)
            #print(curr, curr.children)
            result+= curr.value
            for key in curr.children:
                #print(key, curr.children[key])
                if curr.children[key] and curr.children[key] not in tempQ:
                    tempQ.append(curr.children[key])
        #print('-'*5,'>',result)            
        return result


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)