## 56. Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        ## O(N) - SC; O(N.LogN) - TC
        # intervals.sort()       
        # tempS = [intervals[0]]
        # for pair in intervals[1:]:
        #     if tempS[-1][0] <= pair[0] <= tempS[-1][1]:
        #         tempS[-1][1] = max(pair[1], tempS[-1][1])
        #     else:
        #         tempS.append(pair)       
        #return tempS

        ## O(2) - SC; O(N.LogN) - TC
        intervals.sort()
        N = len(intervals)
        ptr1 = 0
        ptr2 = 1
        while ptr2<N:
            if intervals[ptr1][1]>=intervals[ptr2][0]:
                intervals[ptr1][1] = max(intervals[ptr1][1], intervals[ptr2][1])
            else:
                ptr1+=1
                intervals[ptr1] = intervals[ptr2]
            
            ptr2+=1
            
        intervals[ptr1+1:] = []
        
        # while ptr1<ptr2<N:
        #     #print(ptr1, ptr2)
        #     if intervals[ptr1][0]<= intervals[ptr2][0] <= intervals[ptr1][1]:
        #         intervals[ptr1][1] = max(intervals[ptr2][1],intervals[ptr1][1])
        #         intervals.pop(ptr2)
        #         N-=1
        #         # ptr2+=1
        #     else:
        #         ptr1+=1
        #         ptr2+=1
        
        return intervals