## 739. Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        N = len(temperatures)
        result=[0]*N
        
        ## Monotonic decreasing stack
        tempS = []
        i=0
        while i<N:
            if not tempS:
                tempS.append(i)
            else:
                curr = temperatures[i]
                while tempS and curr>temperatures[tempS[-1]]:
                    prev = tempS.pop()
                    result[prev]= i-prev
                tempS.append(i)
            i+=1
        
        return result
        
        # temp = [[0,temperatures[0]]]
        # idx=1
        # while idx<N and temp:
        #     # print(temp)
        #     while temp and temperatures[idx]>temp[-1][1]:
        #         # print('->',temp)
        #         # print(result[temp[-1][0]], temp[-1][0], idx-temp[-1][0])
        #         result[temp[-1][0]]=idx-temp[-1][0]
        #         # print(result[temp[-1][0]])
        #         temp.pop()
        #     temp.append([idx,temperatures[idx]])
        #     idx+=1
        # print('-'*20)
        # return result
        
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