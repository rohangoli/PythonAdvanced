## Palindrome Pairs

# Example 1:
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

# Example 2:
# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]

# Example 3:
# Input: words = ["a",""]
# Output: [[0,1],[1,0]]

class Trie:
    def __init__(self):
        self._root = {}
    
    def add(self, word, index):
        _iter = self._root
        for char in word:
            if char not in _iter:
                _iter[char] = {}
            _iter = _iter[char]
        _iter["*"] = index
    
    def _dfs_to_leaf(self, trie_node):
        stack = [trie_node]
        result = []
        while stack:
            trie_node = stack.pop()
            for char in trie_node:
                if char == "*":
                    result.append(trie_node[char])
                else:
                    stack.append(trie_node[char])
        return result
                
    def search_indexes(self, word):
        _iter = self._root
        for char in word:
            if char not in _iter:
                return []
            _iter = _iter[char]
        return self._dfs_to_leaf(_iter)

class Solution:
    def is_palindrome(self, word, start, end):
        while start < end:
            if word[start] == word[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
    
    def find_self_palindromes(self, words, skip_index=None):
        result = []

        for i, w in enumerate(words):
            if i == skip_index:
                continue

            if self.is_palindrome(w, 0, len(w)-1):
                result.append(i)
        
        return result
    
    def find_suffix_palindromes(self, words):
        suffix_trie = Trie()
        result = []
        for i, word in enumerate(words):
            if word != "":
                suffix_trie.add(word[::-1], i)
        
        for i, word in enumerate(words):
            suffix_word_indexes = suffix_trie.search_indexes(word)
            for suffix_word_index in suffix_word_indexes:
                if i == suffix_word_index:
                    continue

                probable_word = words[suffix_word_index]
                start_index = 0
                end_index = len(words[suffix_word_index])-len(word)-1
                if self.is_palindrome(probable_word, start_index, end_index):
                    result.append((i, suffix_word_index))

        return result
    
    def find_prefix_palindromes(self, words):
        prefix_trie = Trie()
        result = []
        for i, word in enumerate(words):
            if word != "":
                prefix_trie.add(word, i)

        for i, word in enumerate(words):
            prefix_word_indexes = prefix_trie.search_indexes(word[::-1])
            for prefix_word_index in prefix_word_indexes:
                if i == prefix_word_index:
                    continue

                probable_word = words[prefix_word_index]
                start_index = len(word)
                end_index = len(probable_word)-1
                if self.is_palindrome(probable_word, start_index, end_index):
                    result.append((prefix_word_index, i))

        return result

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = set()
            
        for i, word in enumerate(words):
            if word == "":
                result.update([(i, j) for j in self.find_self_palindromes(words, skip_index=i)])

        result.update(self.find_suffix_palindromes(words))
        result.update(self.find_prefix_palindromes(words))
        
        return result
# class TrieNode:
#     def __init__(self, value=None):
#         self.children = dict()
#         self.value = value

# class Solution:
#     def __init__(self):
#         self.root = TrieNode()
    
#     def insert(self, word, index):
#         curr = self.root
#         for char in word:
#             if char not in curr.children:
#                 curr.children[char] = TrieNode(char)
#             curr = curr.children[char]
         
#         curr.children['*'] = index
        
#     def dfs2leaf(self, trieNode):
#         tempS = [trieNode]
#         result = []
#         while tempS:
#             curr = tempS.pop()
#             for char in curr.children:
#                 if char=='*':
#                     result.append(curr.children[char])
#                 else:
#                     tempS.append(curr.children[char])         
#         return result
    
#     def search(self, word):
#         curr = self.root
#         for char in word:
#             if char not in curr.children:
#                 return []
#             curr = curr.children[char]
#         return self.dfs2leaf(curr)

#     def isPalindrome(self, word, start=0, end=0):
#         while start<end:
#             if word[start]!=word[end]:
#                 return False
#             start+=1
#             end-=1
            
#         return True
    
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
#         results = set()
#         N = len(words)
        
#         ## For empty string + self palindrome combination
#         i=0
#         while i<N-1:
#             j=0
#             while j<N:
#                 if i!=j and words[i]=="" and self.isPalindrome(words[j],0,len(words[j])-1):
#                     results.update([(i,j),(j,i)])
#                 j+=1
#             i+=1
            
#         ## Prefix palidrome 
#         self.root = TrieNode()
#         for idx, word in enumerate(words):
#             self.insert(word, idx)
            
#         for idx, word in enumerate(words):
#             prefix_word_idxs = self.search(word[::-1])
            
#             for prefix_word_idx in prefix_word_idxs:
#                 if idx==prefix_word_idx:
#                     continue
                    
#                 probable_word = words[prefix_word_idx]
#                 start_idx = len(word)
#                 end_idx = len(probable_word)-1
#                 if self.isPalindrome(probable_word, start_idx, end_idx):
#                     results.add((prefix_word_idx,idx))

    
#         ## Suffix palidrome 
#         self.root = TrieNode()
#         for idx, word in enumerate(words):
#             self.insert(word[::-1], idx)
            
#         for idx, word in enumerate(words):
#             suffix_word_idxs = self.search(word)
            
#             for suffix_word_idx in suffix_word_idxs:
#                 if idx==suffix_word_idx:
#                     continue
                    
#                 probable_word = words[suffix_word_idx]
#                 start_idx = 0
#                 end_idx = len(probable_word)-len(word)-1
#                 if self.isPalindrome(probable_word, start_idx, end_idx):
#                     results.add((idx,suffix_word_idx))               
                 
#         return results