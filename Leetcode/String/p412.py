## 412. Fizz Buzz

# Example 1:
# Input: n = 3
# Output: ["1","2","Fizz"]

# Example 2:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]

# Example 3:
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for x in range(1,n+1):
            if x%3==0 and x%5==0:
                result.append("FizzBuzz")
            elif x%3==0:
                result.append("Fizz")
            elif x%5==0:
                result.append("Buzz")
            else:
                result.append(str(x))
                
        return result