## 804. Unique Morse Code Words

# Example 1:
# Input: words = ["gin","zen","gig","msg"]
# Output: 2
# Explanation: The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# There are 2 different transformations: "--...-." and "--...--.".

# Example 2:
# Input: words = ["a"]
# Output: 1

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCodesBase = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morseCodesMap = {chr(k):v for k,v in zip(range(97,123), morseCodesBase)}
        
        #print(morseCodesMap)
        
        result = set()
        
        for word in words:
            temp = ''
            for char in word:
                temp+=morseCodesMap[char]
            result.add(temp)
            
        return len(result)