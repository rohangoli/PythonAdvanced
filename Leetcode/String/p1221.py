## 1221. Split a String in Balanced Strings

# Example 1:
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

# Example 2:
# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

# Example 3:
# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        count = 0
        balance = 0
        N = len(s)
        i=0
        while i<N:
            if s[i]=='L':
                balance+=1
            else:
                balance-=1
                
            if balance == 0:
                count+=1
                
            i+=1
            
        return count
        
#         print('-'*20)
#         ptr = 1
#         N = len(s)
#         result = 0
        
#         while ptr<N:
#             print(ptr-1, s[ptr-1], '-', ptr, s[ptr])
#             temp = 1
#             while ptr<N and s[ptr-1]==s[ptr]:
#                 temp+=1
#                 ptr+=1
#             print('PTR: ', ptr, 'TCount: ',temp)
#             result+=1
#             ptr+=temp+1
#             print('R:',result, 'NPTR:', ptr)
            
#         return result
        
        # ptr1 = 0
        # ptr2 = 1
        # N = len(s)
        # print('-'*20)
        # count = 0
        # curr = s[ptr1]
        # while ptr1<ptr2<N:
        #     print(curr, ptr1,ptr2, s[ptr2])
        #     if curr==s[ptr2]:
        #         ptr2+=1
        #     else:
        #         count+=1
        #         ptr1 = ptr2+1
        #         curr = s[ptr1]
        #         ptr2 = ptr1+1
        # return count
                