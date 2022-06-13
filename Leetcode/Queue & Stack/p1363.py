## Daily Temperatures

# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        N = len(temperatures)
        result=[0]*N
        
        temp = [[0,temperatures[0]]]
        idx=1
        while idx<N and temp:
            # print(temp)
            while temp and temperatures[idx]>temp[-1][1]:
                # print('->',temp)
                # print(result[temp[-1][0]], temp[-1][0], idx-temp[-1][0])
                result[temp[-1][0]]=idx-temp[-1][0]
                # print(result[temp[-1][0]])
                temp.pop()
            temp.append([idx,temperatures[idx]])
            idx+=1
        print('-'*20)
        return result
        
        ## O(N^2) - Rohan's Implementation
#         N = len(temperatures)
#         result = [0]*N
#         i=0
#         while i<N-1:
#             j=i+1
#             while j<N:
#                 if temperatures[i]<temperatures[j]:
#                     result[i]=j-i
#                     break
#                 j+=1               
#             i+=1
            
#         return result

    ## leetcode - Best Time Complexity
    def dailyTemperatures_V2(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [0]
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i-last
            stack.append(i)
        return answer