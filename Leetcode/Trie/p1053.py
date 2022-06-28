## Replace Words / Prefix Hash

# Example 1:
# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"

# Example 2:
# Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# Output: "a a b c"

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isPrefix = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        dictTrie = TrieNode()
        for word in dictionary:
            curr = dictTrie
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                    #print('PARENT:',curr,'>>>> CHILD:', char, curr.children[char])
                curr = curr.children[char]
            curr.isPrefix = True
            #print('isPrefix',curr)
                
        result = []
        for word in sentence.split():
            #print(word)
            curr = dictTrie
            temp = ""
            for char in word:
                if char not in curr.children or curr.isPrefix:
                    break
                temp+=char
                curr = curr.children[char]
            
            if len(temp)>0 and curr.isPrefix:
                result.append(temp)
            else:
                result.append(word)
            
            # if temp=="":
            #     result.append(word)
            # else:
            #     result.append(temp)
        #print('-'*25)
        return " ".join(result)  
                