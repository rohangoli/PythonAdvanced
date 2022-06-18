## Decode String

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

class Solution:
    def decodeString(self, s: str) -> str:
        tempS = []
        
        result = ''
        for x in s:
            # print(tempS)
            if x==']':
                temp = ""
                curr = tempS.pop()
                while curr!='[':
                    temp = curr + temp
                    if tempS:
                        curr = tempS.pop()
                    else:
                        break
                # print('--', tempS)
                mult = ''
                while tempS and tempS[-1].isdigit():
                #while tempS and len(tempS[-1])==1 and 48<=ord(tempS[-1])<=57:
                    mult = tempS.pop() + mult
                mult = int(mult)
                
                tempS.append(temp*mult)
            else:
                tempS.append(x)
        
        while tempS:
            result = tempS.pop() + result

        return result
        
                    