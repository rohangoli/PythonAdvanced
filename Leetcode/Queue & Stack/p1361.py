

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2:
            return False
        
        stack = []
        for x in s:
            if stack and x==')' and stack[-1]=='(':
                stack.pop()
            elif stack and x==']' and stack[-1]=='[':
                stack.pop()
            elif stack and x=='}' and stack[-1]=='{':
                stack.pop()
            else:
                stack.append(x)
            
            # print(stack)

        # print('-'*20)
        if stack:
            return False
        else:
            return True

    ## Best Space Utilization - LeetCode
    def isValid_v2(self, s: str) -> bool:
        stack = []
        hash_map = {')':'(', ']':'[', '}':'{'}
        
        for c in s:
            if c in hash_map:
                if stack != [] and stack[-1] == hash_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        if stack == []:
            return True
        else:
            return False

    ## Best Time Complexity - LeetCode
    def isValid_v3(self, s: str) -> bool:
        
        pairs = {
             ")": "(",
            "]": "[",
            "}": "{"
        }
        right = [')', '}', ']']
        stack = []
        
        for bracket in s:
            if bracket not in right:
                stack.append(bracket)
            elif stack and pairs.get(bracket) == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []
                    