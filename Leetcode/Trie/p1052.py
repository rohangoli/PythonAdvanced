## Add and Search Word - Data structure design

# Example:
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        # self.counter = 0

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord=True

    def search(self, word:str, curr = None, j=0) -> bool:
        
        curr = (curr if curr else self.root)
        for i in range(j,len(word)):
            if word[i]=='.':
                for child in curr.children:
                    if self.search(word, curr.children[child],i+1):
                        return True
                return False
            else:
                if word[i] not in curr.children:
                    return False
                curr = curr.children[word[i]]
                
        return curr.isWord
        
    def search_old(self, word: str) -> bool:
        self.counter+=1
        print("SEARCH: ",self.counter)
        curr = self.root
        i=0
        N = len(word)
        
        while i<N:
            char = word[i]
            while char=='.':
                print([child for child in curr.children])
                tempS = [curr.children[child] for child in curr.children]
                print(tempS)
                while tempS:
                    curr = tempS.pop()
                    j=i+1
                    while j<N:
                        char2 = word[j]
                        print(char2)
                        if char2=='.':
                            j+=1
                            break
                        elif char2 not in curr.children and tempS==[]:
                            return False
                        elif char2 not in curr.children:
                            break
                        curr = curr.children[char2]
                        j+=1
                    if curr.isWord:
                        return True
            if char not in curr.children:
                return False
            curr = curr.children[char]
            i+=1
            
#         while i<N:
#             char = word[i]
#             print([child for child in curr.children])
#             tempS = [curr.children[child] for child in curr.children]
#             print(tempS)
#             while char=='.' and tempS:
#                 curr = tempS.pop()
#                 j=i+1
#                 while j<N:
#                     char2 = word[j]
#                     print(char2)
#                     if char2 not in curr.children and tempS==[]:
#                         return False
#                     elif char2 not in curr.children:
#                         break
#                     curr = curr.children[char2]
#                     j+=1
#                 if curr.isWord:
#                     return True
#             if char not in curr.children:
#                 return False
#             curr = curr.children[char]
#             i+=1
        
#         if curr.isWord==True:
#             return True
#         else:
#             return False
            
        
            
#         for char in word:
#             if char in curr.children:
#                 curr = curr.children[char]
#             elif char=='.':
                
#                 temp = list(curr.children.keys())
#                 #print(temp)
#                 if temp:
#                     curr = curr.children[temp[0]]
#                 else:
#                     return False
#             else:
#                 return False
#         if curr.isWord==True:
#             return True
#         else:
#             return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)