class TrieNode:
    def __init__(self, value):
        self.value = value
        self.child = dict()

class Trie:
    def __init__(self, value=0):
        self.root = TrieNode(value)
        
    def insert(self, word):
        ## Insert word
        curr = self.root
        for char in word:
            if char not in curr.child:
                curr.child[char] = TrieNode(char)
            curr = curr.child[char]
        # curr.isWord = True
        
        # Insert Reverse word
        curr = self.root
        for char in word[::-1]:
            if char not in curr.child:
                curr.child[char] = TrieNode(char)
            curr = curr.child[char]
        # curr.isWord = True
        
    def search(self, word):
        print('Prefix SEARCH: ', word)
        curr = self.root
        for char in word:
            # print(char, curr.child)
            if char not in curr.child:
                print(word, 'NOT FOUND')
                return False
            curr = curr.child[char]
        print(word, 'FOUND')    
        return True

    def inverse_search(self, word):
        print('Suffix INVERSE SEARCH: ', word)
        curr = self.root
        for char in word[::-1]:
            # print(char, curr.child)
            if char not in curr.child:
                print(word, 'NOT FOUND')
                return False
            curr = curr.child[char]
        print(word, 'FOUND')    
        return True        
    
        
def prefixSuffixString(s1, s2) -> int:
    tempTrie = Trie()
    for word in s1:
        tempTrie.insert(word)
        
    result = 0
    for word in s2:
        if tempTrie.search(word) or tempTrie.inverse_search(word):
            result+=1
        # print('-'*10)
    return result
    # print(tempTrie.root.child)

print('TC1')
print(prefixSuffixString(["cat", "catanddog", "lion"], ["cat", "dog", "rat"]))

s1 = ["jrjiml", "tchetn", "ucrhye", "ynayhy", "cuhffd", "cvgpoiu", "znyadv"]
s2 = ["jr", "ml", "cvgpoi", "gpoiu", "wnmkmluc", "geheqe", "uglxagyl", "uyxdroj"] 
print('TC2')
print(prefixSuffixString(s1, s2))