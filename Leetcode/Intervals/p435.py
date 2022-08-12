## 435. Non-overlapping Intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        # print(intervals)
        
        prevEnd = intervals[0][1]
        result = 0
        for start, end in intervals[1:]:
            if start>=prevEnd:
                prevEnd = end
            else:
                result+=1
                prevEnd = min(end, prevEnd)
        
        return result
        
#         ptr1 = 0
#         ptr2 = 1
#         merges = 0

#         while ptr2<len(intervals):
#             if intervals[ptr1][1]>intervals[ptr2][0]:
#                 merges+=1
#             else:
#                 ptr1+=1
                
#             ptr2+=1
        
#         return merges