## 57. Insert Interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        N = len(intervals)
        insert = False
        while i<N:
            if intervals[i][0]>= newInterval[0]:
                intervals.insert(i, newInterval)
                insert = True
                break
            i+=1
            
        if not insert:
            intervals.append(newInterval)
            
        #print(intervals)
        ptr1=0
        ptr2=1
        while ptr2<N+1:
            #print(ptr1, ptr2)
            #print(intervals[ptr1], intervals[ptr2])
            if intervals[ptr1][1]>=intervals[ptr2][0]:
                intervals[ptr1][1]=max(intervals[ptr1][1], intervals[ptr2][1])
            else:
                ptr1+=1
                intervals[ptr1] = intervals[ptr2]
            ptr2+=1
            
        #print(intervals)
        intervals[ptr1+1:]=[]
        
        return intervals