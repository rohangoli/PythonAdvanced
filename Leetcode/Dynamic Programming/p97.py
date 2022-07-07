## 97. Interleaving String

## Solutions: https://leetcode.com/problems/interleaving-string/solution/

# Example 1:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true

# Example 2:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false

# Example 3:
# Input: s1 = "", s2 = "", s3 = ""
# Output: true

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3): return False
        
        @lru_cache(None)
        def helper(i,j,k):
            if k<0: return True
            if i<0: return s2[:j+1]==s3[:k+1]
            if j<0: return s1[:i+1]==s3[:k+1]
            
            n1, n2 = False, False
            if s1[i]==s3[k]:
                n1 = helper(i-1,j,k-1)
            if s2[j]==s3[k]:
                n2 = helper(i,j-1,k-1)

            return any((n1,n2))
            
        return helper(len(s1)-1, len(s2)-1, len(s3)-1)
        
    def isInterleave_v3(self, s1: str, s2: str, s3: str) -> bool:
        if not s3:
            return not (s1 or s2)
        
        if s1 and s1[0]==s3[0] and (not s2 or s2[0]!=s3[0]):
            return self.isInterleave(s1[1:],s2,s3[1:])
        
        if s2 and s2[0]==s3[0] and (not s1 or s1[0]!=s3[0]):
            return self.isInterleave(s1,s2[1:],s3[1:])
        
        if s1 and s2 and s1[0]==s2[0]==s3[0]:
            return self.isInterleave(s1[1:],s2,s3[1:]) or self.isInterleave(s1,s2[1:],s3[1:])
        
        return False
        
    def isInterleave_v2(self, s1: str, s2: str, s3: str) -> bool:
        print('-'*25)
        print('{} + {} = {}'.format(s1,s2,s3))
        def helper(s1, s2, s3):
            print('-'*10)
            X = len(s1)
            Y = len(s2)
            Z = len(s3)
            if Z==0:
                return True

            if X+Y!=Z:
                return False

            ptr1=0
            ptr2=0
            ptr3=0
            while ptr3<Z and (ptr1<X or ptr2<Y):
                while ptr1<X and ptr3<Z and s3[ptr3]==s1[ptr1]:
                    print("Condition 1 >>> PTRs: ({},{}), Values:({},{})".format(ptr1, ptr3, s1[ptr1], s3[ptr3]))
                    ptr1+=1
                    ptr3+=1

                while ptr2<Y and ptr3<Z and s3[ptr3]==s2[ptr2]:
                    print("Condition 2 >>> PTRs: ({},{}), Values:({},{})".format( ptr2, ptr3, s2[ptr2], s3[ptr3]))
                    ptr2+=1
                    ptr3+=1

                if ptr3<Z:
                    if ptr1<X and ptr2<Y and s3[ptr3]!=s1[ptr1] and s3[ptr3]!=s2[ptr2]:
                        return False
                    elif ptr1<X and ptr2==Y and s3[ptr3]!=s1[ptr1]:
                        return False
                    elif ptr2<Y and ptr1==X and s3[ptr3]!=s2[ptr2]:
                        return False
                # ptr3+=1

            return True
        
        return helper(s1, s2, s3) or helper(s2, s1, s3)