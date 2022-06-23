##  Implement Trie (Prefix Tree)

# Example 1:
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        #print('-'*30)

    def insert(self, word: str) -> None:
        #print('insert:start')
        curr = self.root
        for char in word:
            #print(curr.children)
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True
        #print("insert", word)

    def search(self, word: str) -> bool:
        #print("search:start")
        curr = self.root
        for char in word:
            #print(curr.children)
            if char not in curr.children:
                #print('search: FALSE')
                return False
            curr = curr.children[char]
        
        if curr.isWord:
            #print('search: TRUE')
            return True
        else:
            #print('search: FALSE')
            return False
        

    def startsWith(self, prefix: str) -> bool:
        #print("startWith:start")
        curr = self.root
        for char in prefix:
            #print(curr.children)
            if char not in curr.children:
                #print('startsWith: FALSE')
                return False
            curr = curr.children[char]
        #print('startsWith: TRUE')    
        return True
      


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)