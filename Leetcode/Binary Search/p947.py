## First Bad Version

# Example 1:
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.

# Example 2:
# Input: n = 1, bad = 1
# Output: 1

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        
        if (end-start)<0:
            return n
        
        while start<end:
            mid = start + (end-start)//2
            #print(start, mid, end)
            if isBadVersion(mid):
                end = mid
            else:
                start = mid+1
        
        #print('-'*5, start,n)
        if isBadVersion(start):
            return start
        return -1