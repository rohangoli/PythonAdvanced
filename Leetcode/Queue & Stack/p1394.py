## Evaluate Reverse Polish Notation

# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Example 2:
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

# Example 3:
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for x in tokens:
            if x in ['+','-','*','/'] and stack:
                B = stack.pop()
                A = stack.pop()
                # print(A,B,x)
                # print(type(A), type(B), type(x))
                stack.append(str(int(eval(A+x+B))))
            else:
                stack.append(x)
                
        return stack[0]